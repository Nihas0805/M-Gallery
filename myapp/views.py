from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import MovieForm

from myapp.models import Movies

from django.contrib import messages


class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)

            Movies.objects.create(**data)

            messages.success(request,"movie has been added")

            return redirect("movie-list")
        
        else:

            messages.error(request,"cannot add movie")

            return render(request,"movie_add.html",{"form":form_instance})


class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movies_list.html",{"movies":qs})



class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"movie":qs})



class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id).delete()

        messages.error(request,"movie has been deleted successfully")

        return redirect("movie-list")


class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id)

        movie_dict={
            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director,
        }

        form_instance=MovieForm(initial=movie_dict)

        return render(request,'movie_edit.html',{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Movies.objects.filter(id=id).update(**data)

            messages.success(request,"movie has be updated successfully")

            return redirect("movie-list")

        else:
            return render(request,'movie_edit.html',{"form":form_instance})

            messages.error(request,"movie cannot be updated")


    
    











