from django import forms

class CinemaHallForm(forms.Form):
    cinemahall_name          =forms.CharField(label="Enter cinemahall name",max_length=50)
    cinemahall_address       =forms.CharField(label="Enter cinemahall address",max_length=100)
    seats                    =forms.CharField(label="Enter number of seats ",max_length=100)
    timing                   =forms.CharField(label="Enter the show timings",max_length=100)
    cinemahall_place         =forms.CharField(label="Enter the place",max_length=100)
    cinemahall_contactinfo   =forms.CharField(label="Enter contact number",max_length=10)
    current_movie            =forms.CharField(label="Present movie running in the theatre",max_length=50)
    cinemahall_image         =forms.ImageField(label="choose image")
