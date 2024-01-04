# WeatherML
## Background
One unique thing about me is that I love my black Adidas jacket and I wear it as
much as I can. My default style is to leave it unzipped with rolled-up sleeves.
However, the weather can change that. If it's chilly, I may roll down the
sleeves or zip up. I may even need to wear a coat. If it's too hot, it can be
uncomfortable to have it on at all.

The idea for this project started when I was a first-year college student. As
someone living on-campus, I had to walk to my classes. In addition, as a student
at Virginia Tech, I would be crossing the Drillfield every time, exposing me to
the elements. As a result, I got in the habit of checking the weather every time
when I had to go somewhere (I even ended up adding a temperature widget to my
lock screen since I checked the weather so many times). The problem was that
predicting my choice of outerwear wasn't straightforward. There would be days
when I could go out with just a T-shirt when it was only 65. On others, I would
need a coat even though it was 73.

Obviously, temperature is not the only factor in comfort. Wind, humidity, and
whether the sun is shining can all affect how warm or cold I feel. However, it's
very hard for me to make a prediction while juggling all the different factors.
As a result, I thought about potentially coding some sort of AI that could read
the weather and give me a prediction on what I should wear outside. Thus, the
idea for *WeatherML* was born.

## Data Collection
At the start, I didn't have any experience or knowledge to code a ML model.
However, I knew I would need a lot of data, so I started collecting data right
away. I included as many factors that I thought might be relevant, and tried to
collect several times a day (morning, noon, evening). My source of data was just
the Weather app on my iPhone. Although I've heard that it's not the most
accurate source for weather information, it was the most convenient for me.
Besides, I used the Weather app anyways to check the weather so I trusted that
the ML model would be able to handle the inaccuracies. I record my data in
[this Google sheet](https://docs.google.com/spreadsheets/d/1wjoOM3OyRlOUdET7_jU2uoCyOraQOWY8XGOw8LVWK3A/edit?usp=sharing)
and then download it as a CSV when I'm ready for another round of training.

## The Model
I learned the basic concepts of AI models in a course I took at Virginia Tech:
*CS4804: Intro to Artificial Intelligence*. However, I learned how to actually
code them via LinkedIn Learning courses (check out my
[LinkedInLearning](https://github.com/tikkikkit21/LinkedInLearning)
repository for notes and exercise files from courses I've taken. Most of the ML
courses are under the *Python* folder).

I use `pandas` to import data and `scikit-learn` for dataset preparation and
training. As of current (with v1 of the dataset), I have a training accuracy of
73.47% and test accuracy of 81.82%. It's not terrible, but I definitely want to
improve it (my goal is ~90% for both is possible). The model itself will need to
be tweaked, but the biggest thing I'll need to do is collect a lot more data.
