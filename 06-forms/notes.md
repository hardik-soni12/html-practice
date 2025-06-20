# HTML Forms - notes  
  
## Form Tag:  
▫️&lt;form action="" method=""&gt;  
▫️action: Where data will be sent.  
▫️method: GET (visible in URL) or POST (hidden).  
  
## Common Input Types:  
▫️text: Single-line text input.  
▫️email: validates email format.  
▫️password: Hidden characters.  
▫️number: Only numeric values.  
▫️date: Date picker.  
▫️file: Upload files.  
▫️color: Color picker.  
  
## Special Inputs:  
▫️&lt;textarea&gt; : For long text/multi-Line.  
▫️&lt;select&gt; with &lt;option&gt; : Dropdown list.  
▫️&lt;input type="radio"&gt; : Choose one from a group.  
▫️&lt;input type="checkbox"&gt; : Choose multiple options.  
  
## Layout Tags:  
▫️&lt;fieldset&gt; : Groups form fields.  
▫️&lt;legend&gt; : Title for a fieldset.  
▫️&lt;label&gt; : Descibes input; use for="id" to link it.  
▫️&lt;button&gt; or &lt;input type="submit"&gt; : for form submission.  
  
  --

▫️Use name="" attribute for input fields to make them submit data correctly.  
  
## Iframe (Embedded content):  
~~ &lt;iframe src="https://example.com" width="600" height="400"&gt;&lt;/iframe&gt;  
▫️Use to embed Youtube, Maps, or External sites.  
▫️Add title for accessibility.  
▫️allowfullscreen to support full-screen videos.  
  
## &lt;video&gt; tag:  
▫️The video tag is used to embed video content directly in a webpage without third-party plugins.
  
~~ Common Attributes for video tag:  
▫️src : path to the video file.  
▫️controls : shows default play/pause/volume contols.  
▫️autoplay : starts playing automatically.  
▫️muted : mutes the video (needed for autoplay to work).  
▫️loop : Repeats the video.  
▫️poster : image shown before the video loads.  
▫️weight/height : size of the video player.  
  
--  