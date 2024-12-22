# Olympics-Dashboard
Power BI dashboard that pulls ongoing olympics and  historical data from kaggle using a Python Script and shows real time insights into performance of Athletes and Countries for all events.

** Visualizations, Widgets & Tools Used : 
Bar Charts, Share Map, Cards, Tile Slicer, Donut Charts, Text Filter (for search functionality), Page Navigator Button & Bookmarks (to create navigators).

** DAX used to create measures in order to get :
medal count (based on medallist country/Age group/medal type/athlete gender),No. of participating Nations,Teams, Athletes and Key tournament highlights.

** Pandas and python File Handling to fetch data from Kaggle.

** Sections of Dashboard: 
-Overview : Shows Key highlights, important figures like medal/country/teams/athletes count wit slicers for countries & Sport events.
-Athletes : Shows Athlete information based on Age,gender,medal type with a search functionality to search a particular Athlete and slicers for Sport events.
-Country : Shows geographical location of a country on Share map visualization with search functionality to search a particular Country and slicers for Sport events.
-Historical : Shows historical data of all olympic editions from 1896-2020 with slicers for Countries,Sport Events,Olympic Year and Search functionality for participating Countries over all editions of Olympics.
