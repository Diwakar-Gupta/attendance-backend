from django.contrib import admin
from django.urls import reverse
from attendance.models import (
    Student,
    Subject,
    SubjectClass,
    ClassAttendance,
    ProjectConfiguration,
    GeoLocationDataContrib,
    ClassAttendanceWithGeoLocation,
    FalseAttemptGeoLocation,
    ClassAttendanceByBSM,
    ProblemSolvingPercentage,
)

# Register your models here.


class ClassAttendanceWithGeoLocationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "status",
    )
    list_filter = (
        "status",
        "class_attendance__subject",
        "class_attendance__student",
    )  # Add the fields you want to use as filters
    list_editable = ("status",)


class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "attendance_status")
    list_filter = ("subject", "attendance_status", "student")
    autocomplete_fields = ["student"]


class FalseAttemptAdmin(admin.ModelAdmin):
    list_display = ("__str__", "verify")
    list_filter = ("subject", "student")  # Add the fields you want to use as filters

    def verify(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" target="_blank" href="{}">Verify</a>',
            reverse("verify_false_attempt", args=[obj.pk]),
        )


class ClassAttendanceByBSMAdmin(admin.ModelAdmin):
    list_display = ("__str__", "status")  # Add the fields you want to use as filters
    list_filter = (
        "status",
        "class_attendance__subject",
        "class_attendance__student",
    )  # Add the fields you want to use as filters
    list_editable = ("status",)


class ProblemSolvingPercentageAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject",
        "percentage",
        "solved_questions",
        "total_questions",
    )

    def percentage(self, obj):
        if obj.total_questions == 0:
            return 0
        return int((obj.solved_questions / obj.total_questions) * 100)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "mail", "show_attendance", "send_notification")
    search_fields = ["name", "mail"]

    def show_attendance(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" target="_blank" href="{}">Show Attendance</a>',
            reverse("studentAttendance", args=[obj.mail.split("@")[0]]),
        )

    def send_notification(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" {} target="_blank" href="{}">Send Notification</a>',
            "disabled" if not obj.fcmtoken else "",
            reverse("sendNotification", args=[obj.pk]),
        )

    send_notification.short_description = "Send Reminder"


class SubjectClassAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "is_attendance_mandatory",
        "injest_to_scaler",
        "mark_attendance",
        "send_reminder",
    )
    save_as = True
    search_fields = ["name"]

    def mark_attendance(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" target="_blank" href="{}">Mark Attendance</a>',
            reverse("getAttendanceView", args=[obj.pk]),
        )

    def injest_to_scaler(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" target="_blank" href="{}">Injest to Scaler</a>',
            reverse("injest_to_scaler", args=[obj.pk]),
        )

    def send_reminder(self, obj):
        from django.utils.html import format_html

        return format_html(
            '<a class="button" target="_blank" href="{}">Remind Absenties</a>',
            reverse("sendReminderForClass", args=[obj.pk]),
        )

    def has_change_permission(self, request, obj=None):
        from django.utils import timezone

        current_time = timezone.now()

        if (
            obj is not None
            and obj.class_end_time < current_time
            and not request.user.is_superuser
        ):
            return False
        return super().has_change_permission(request, obj=obj)


admin.site.register(ProblemSolvingPercentage, ProblemSolvingPercentageAdmin)
admin.site.register(ClassAttendanceByBSM, ClassAttendanceByBSMAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(SubjectClass, SubjectClassAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
admin.site.register(GeoLocationDataContrib)
admin.site.register(ClassAttendanceWithGeoLocation, ClassAttendanceWithGeoLocationAdmin)
admin.site.register(FalseAttemptGeoLocation, FalseAttemptAdmin)
admin.site.register(ProjectConfiguration)
admin.site.register(Subject)
