# Image Recognition Reverse

This is a personal side project that doing image recognition by using captions in google reverse image look up, inspired by Peter Norvig's presentation: [The Unreasonable Effectiveness of Data](https://www.youtube.com/watch?v=yvDCzhbjYWs)

###About
  - Given an url for any image.
  - Return a list of most likely descriptions for the image.
<br>

This is done by:

 1. Using google reverse image to look up given url.
 2. Find list of similar images.
 3. Extract result images captions and title info.
 4. Clean and parse the image info to get final frequency rank.


###Examples:
 ![Google owned Boston Dynamics Robot Wildcat ](http://www.blogcdn.com/www.engadget.com/media/2012/09/boston-dynamics-alphadog-ls3-darpa-demo.jpg)
<br>url:http://www.blogcdn.com/www.engadget.com/media/2012/09/boston-dynamics-alphadog-ls3-darpa-demo.jpg<br>
Top three results: **robot, military, google**

<br> ![Lionel Messi](http://i0.wp.com/akihabarablues.com/wp-content/uploads/2015/09/messi1.jpg)
<br>
url:http://i0.wp.com/akihabarablues.com/wp-content/uploads/2015/09/messi1.jpg<br>
Top three results: **messi, lionel, barcelona**


<br> ![Rei Ayanami from Evangelion](http://vignette1.wikia.nocookie.net/evangelion/images/1/12/Rei_Ayanami_OP.png)
<br>
url:http://vignette1.wikia.nocookie.net/evangelion/images/1/12/Rei_Ayanami_OP.png<br>
Top three results: **rei, evangelion , ayanami**
 

### Version
0.07

### Todos

 - Deeper clean process(adverb/verb etc.)
 - Larger amount of data
 - Using result words to form meaningful sentence.  
 - Making this a web app using Python/Flask.
 - Enable local image upload. 



License
----

MIT
