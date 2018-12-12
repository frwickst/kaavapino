from rest_framework import serializers


class ProjectTimelineEntrySerializer(serializers.Serializer):
    content = serializers.CharField()
    start = serializers.DateTimeField()
    end = serializers.DateTimeField()
    group = serializers.CharField()
    type = serializers.SerializerMethodField()
    classname = serializers.SerializerMethodField()

    def get_type(self):
        return "background"

    def get_classname(self):
        return "#F0F0F0"

    class Meta:
        fields = ["content", "start", "end", "group", "type", "classname"]
