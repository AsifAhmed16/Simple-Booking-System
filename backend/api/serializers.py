from datetime import datetime

from rest_framework import serializers

from .models import VacancyList, BookingEntry


class VacancyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyList
        fields = '__all__'


class BookingEntrySerializer(serializers.ModelSerializer):
    vacancy_serializer = VacancyListSerializer()

    class Meta:
        model = BookingEntry
        fields = '__all__'

    def create(self, validated_data):
        start_date = validated_data.pop('start_date')
        end_date = validated_data.pop('end_date')

        from_date = datetime.strptime(start_date, "%Y-%m-%d")
        to_date = datetime.strptime(end_date, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)

        while from_date <= to_date:
            if not VacancyList.objects.filter(selected_date=from_date).exists():
                vacancy = VacancyList.objects.create(selected_date=from_date)
                vacancy.save()
            from_date += delta

        booking = BookingEntry.objects.create(**validated_data)
        return booking
