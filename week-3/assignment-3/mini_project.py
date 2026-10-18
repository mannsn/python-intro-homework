#Cover at least 3 days × 3 times = 9 combinations with distinct suggestions
#Handle any unrecognized day or time with a friendly fallback message
#Normalize input so capitalization doesn't matter (e.g., "Monday" and "monday" both work)


day = (input("What day is it? Input: Monday/Mon Tuesday/Tue Wednesday/Wed "))
lower_day = day.lower()


time_of_day = (input( "What time of day? Input: morning or afternoon or evening: "))
lower_time_of_day = time_of_day.lower()


if ((lower_day == "monday" or lower_day == "mon") and (lower_time_of_day == "morning")):
    print(f"On {day} {time_of_day} make Python announcement - remind everyone what is due!")
elif ((lower_day == "monday" or lower_day == "mon") and (lower_time_of_day == "afternoon")):
    print(f"On {day} {time_of_day} take a nap!")
elif ((lower_day == "monday" or lower_day == "mon") and (lower_time_of_day == "evening")):
    print(f"On {day} {time_of_day} study Hungarian on duolingo!")

elif ((lower_day == "tuesday" or lower_day == "tue") and (lower_time_of_day == "morning")):
    print(f"On {day} {time_of_day} do some exercise!")
elif ((lower_day == "tuesday" or lower_day == "tue") and (lower_time_of_day == "afternoon")):
    print(f"On {day} {time_of_day} read a book!")
elif ((lower_day == "tuesday" or lower_day == "tue") and (lower_time_of_day == "evening")):
    print(f"On {day} {time_of_day} play Splendor duel!")

elif ((lower_day == "wednesday" or lower_day == "wed") and (lower_time_of_day == "morning")):
    print(f"On {day} {time_of_day} go kayaking!")
elif ((lower_day == "wednesday" or lower_day == "wed") and (lower_time_of_day == "afternoon")):
    print(f"On {day} {time_of_day} sew a project!")
elif ((lower_day == "wednesday" or lower_day == "wed") and (lower_time_of_day == "evening")):
    print(f"On {day} {time_of_day} take dog on a walk!")

elif (lower_day != "monday" and  lower_day != "mon" and lower_day != "tuesday" and lower_day != "tue" and lower_day != "wednesday" and lower_day != "wed" ):
     print (f"Sorry, I don't recognize the day {day}. Try Monday/Mon Tuesday/Tue Wednesday/Wed ") 

elif (lower_time_of_day != "morning" or lower_time_of_day != "afternoon" or lower_time_of_day != "evening"):
     print (f"Sorry, I don't recognize time of day {time_of_day}. Try morning or afternoon or evening")
