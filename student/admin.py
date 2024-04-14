import nested_admin
from django.contrib import admin

# Register your models here.
from student.models import Student, Contact, ExamInfo, ExamDetailInfo


# TabularInline 表格形式的展示
class ContactAdmin(nested_admin.NestedTabularInline):
    # 展示指定内容
    list_display = ['id', 'info', 'alert']
    model = Contact
    extra = 0  # 默认不展示


class ExamDetailInfoAdmin(nested_admin.NestedTabularInline):
    model = ExamDetailInfo
    extra = 0  # 默认不展示


# NestedStackedInline 上下排版
class ExamInfoAdmin(nested_admin.NestedStackedInline):
    model = ExamInfo
    extra = 0  # 默认不展示
    inlines = [ExamDetailInfoAdmin]


# ModelAdmin 常规展示
class StudentAdmin(nested_admin.NestedModelAdmin):
    # 展示指定内容
    list_display = ['id', 'studentName', 'studentAge']
    model = Student
    inlines = [ContactAdmin, ExamInfoAdmin]  # 嵌套在页面里

    actions = ['test_btn']  # 批量按钮定义
    @admin.action(permissions=['changs'])  # 权限定义
    def test_btn(self,httprequest,queryset):
        print("请求信息", httprequest)
        print("页面选择的数据信息", queryset)
        self.message_user(httprequest,'执行成功')  # 前端提示


    test_btn.short_description = '测试按钮'
    test_btn.confirm = '这是一个对话框，你确定要执行这个按钮的动作吗?'

# admin.site.register(Contact, ContactAdmin)
admin.site.register(Student, StudentAdmin)
