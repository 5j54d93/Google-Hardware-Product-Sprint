# Dashboard（web）of our project

- real time
- Github doc link
- day／night mode
- smart information
- auto：watering、noising
- remote control：watering、noising

## Overview

1. [Screenshot with Day theme and Nithgt theme](https://github.com/5j54d93/Google-HPS/tree/main/templates#screenshot-with-day-theme-and-nithgt-theme)
2. [Using Bootstrap to design web frontend](https://github.com/5j54d93/Google-HPS/tree/main/templates#using-bootstrap-to-design-web-frontend)
   - [top title and time display](https://github.com/5j54d93/Google-HPS/tree/main/templates#top-title-and-time-display)
   - [information cards](https://github.com/5j54d93/Google-HPS/tree/main/templates#information-cards)
   - [footer](https://github.com/5j54d93/Google-HPS/tree/main/templates#footer)
   - [Auto switching between Day theme and Night theme](https://github.com/5j54d93/Google-HPS/tree/main/templates#auto-switching-between-day-theme-and-night-theme)
3. [Web feature](https://github.com/5j54d93/Google-HPS/tree/main/templates#web-feature)

## Screenshot with Day theme and Nithgt theme

<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/Screenshot.png" width='100%' height='100%'/>

## Using [Bootstrap](https://bootstrap5.hexschool.com/docs/5.0/getting-started/introduction/) to design web frontend

### [top title](https://bootstrap5.hexschool.com/docs/5.0/examples/features/) and time display

```html
<h1 class="pb-2 border-bottom">
    <span class="text-primary">G</span><span class="text-danger">o</span><span class="text-warning">o</span><span class="text-primary">g</span><span class="text-success">l</span><span class="text-danger">e</span>
    HPS Team 2：Demeter<span class='fs-4 float-end mt-4'>{{year}} 年 {{month}} 月 {{day}} 日  {{hour}}：{{min}}</span>
</h1>
```

### information [cards](https://bootstrap5.hexschool.com/docs/5.0/components/card/)

```html
<div class="col-sm-3">
    <div class="card day light">
        <div class="card-body">
            <h4 class="card-title p-3 mb-2 day cardtitle">
                <svg xmlns="http://www.w3.org/2000/svg" width="1.2em" height="1.2em" fill="#0dcaf0" class="bi bi-moisture" viewBox="0 0 18 18">
                    <path d="M13.5 0a.5.5 0 0 0 0 1H15v2.75h-.5a.5.5 0 0 0 0 1h.5V7.5h-1.5a.5.5 0 0 0 0 1H15v2.75h-.5a.5.5 0 0 0 0 1h.5V15h-1.5a.5.5 0 0 0 0 1h2a.5.5 0 0 0 .5-.5V.5a.5.5 0 0 0-.5-.5h-2zM7 1.5l.364-.343a.5.5 0 0 0-.728 0l-.002.002-.006.007-.022.023-.08.088a28.458 28.458 0 0 0-1.274 1.517c-.769.983-1.714 2.325-2.385 3.727C2.368 7.564 2 8.682 2 9.733 2 12.614 4.212 15 7 15s5-2.386 5-5.267c0-1.05-.368-2.169-.867-3.212-.671-1.402-1.616-2.744-2.385-3.727a28.458 28.458 0 0 0-1.354-1.605l-.022-.023-.006-.007-.002-.001L7 1.5zm0 0-.364-.343L7 1.5zm-.016.766L7 2.247l.016.019c.24.274.572.667.944 1.144.611.781 1.32 1.776 1.901 2.827H4.14c.58-1.051 1.29-2.046 1.9-2.827.373-.477.706-.87.945-1.144zM3 9.733c0-.755.244-1.612.638-2.496h6.724c.395.884.638 1.741.638 2.496C11 12.117 9.182 14 7 14s-4-1.883-4-4.267z"/>
                </svg>
                &nbsp;濕度 Humidity
                </h4>
	            <p class="card-text">{{dry_or_wet_plant}}</p>
	            <p class="card-text">{{dry_or_wet_people}}</p>
	    </div>
        <ul class="list-group list-group-flush">
            <li class="list-group-item day light"><span class="fw-bold">・濕度：</span>{{humidity}} ％</li>
        </ul>
        <div class="card-body">
	        <form method="post" action="/">
	            <input class="btn btn-primary" type="submit" value="Watering" name="Watering"/>
                <button type="button" class="btn btn-dark">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                    <a href="https://github.com/5j54d93/Google-HPS/blob/0cb360f645171c22623b129981b8182c14857a27/temperature_humidity/SHT31D.py#L31" class="text-white bg-dark" style="text-decoration:none;" target="_blank">
                    Doc
                    </a>
                </button>
	        </form>
        </div>
    </div>
</div>
```

### [footer](https://bootstrap5.hexschool.com/docs/5.0/examples/album/)

```html
<footer class="text-muted py-3 border-top">
    <div class="container">
        <p class="float-end mb-1">
      	    <button type="button" class="btn btn-dark border border-white">
            	<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
            		<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
            	<a href="https://github.com/5j54d93/Google-HPS/tree/cbdedf58fc93fe9c6ef6ab69733e685fb0193184" class="text-white bg-dark" style="text-decoration:none;" target="_blank">
            	GitHub
           		</a>
          	</button>
    	</p>
    	<p class="mb-1">© Google Hardware Product Sprint 2021</p>
    	<p class="mb-0">APAC TW HPS Program：Team 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mentor：Weihsuan</p>
  	</div>
</footer>
```

### Auto switching between Day theme and Night theme

```CSS
<style>
    .day { background-color: #fff; color: #000; }
        
    @media (prefers-color-scheme: light) { .day.cardtitle { background-color: #F8F9FA; } }
        
    @media (prefers-color-scheme: dark) {
        .day.night {
    		background-color: #22272E;
      		border-color: #434C56;
    		color: #fff;
  		}
      	.day.light {
    		background-color: #373E47;
      		border-color: #ADBAC7;
    		color: #ADBAC7;
  		}
      	.day.cardtitle {
    		background-color: #495057;
      		color: #fff;
  		}
    }
</style>
```

## Web feature

<img src="https://github.com/5j54d93/Google-HPS/blob/main/photo/web%20feature.png" width='100%' height='100%'/>
