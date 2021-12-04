from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import VacancyList, BookingEntry

# Global variables for default values.
# Day costing considering 100.00/-.
COST_PER_DAY = 100.00
# considering default vacant number = 5.
SET_VACANCY_LIMIT = 5


class BookingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = self.request.data.copy()

            start_date = data['from_date']
            end_date = data['to_date']
            from_date = datetime.strptime(start_date, "%Y-%m-%d")
            to_date = datetime.strptime(end_date, "%Y-%m-%d")
            delta = timedelta(days=1)
            day_counter = 0

            while from_date <= to_date:
                vacancy_obj = VacancyList.objects.filter(selected_date=from_date)
                if vacancy_obj.exists():
                    available_vacancy = VacancyList.objects.get(selected_date=from_date).no_of_vacancy
                    if available_vacancy > 0:
                        available_vacancy -= 1
                        vacancy_obj.update(no_of_vacancy=available_vacancy)
                    else:
                        err_msg = "No vacancy for date - " + str(from_date)
                        return Response({'msg': err_msg}, status=status.HTTP_403_FORBIDDEN)
                else:
                    VacancyList.objects.create(selected_date=from_date, no_of_vacancy=SET_VACANCY_LIMIT-1)
                day_counter += 1
                from_date += delta

            BookingEntry.objects.create(start_date=start_date, end_date=end_date, total_cost=(day_counter * COST_PER_DAY))
            return Response({'msg': 'Booked Successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'msg': 'Exception'}, status=status.HTTP_400_BAD_REQUEST)
