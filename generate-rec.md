# Generating Recs from Data

After the similar product engine is built, the system enters training, and finally serving functionality. To generate a rec the system uses the pattern below. Specific to the Spotify Million Playlist challenge, 

items = spotify tracks already in the playlist

categories = selected metadata from the playlist, including the following rows : playlist_name, album_uri, artist_uri, track_name, album_name, artist_name, track_uri

num= 500 tracks to recommend

blacklist = spotify tracks already in the playlist

### query for main track spotify playlist completion:

```
curl -H "Content-Type: application/json" \
-d '{"items": ["spotify:track:0gWmxML0Fc6z9e5adPqi1s","spotify:track:0JWeCKQU60BPmDkYFa9zN3","spotify:track:0m6i2lZNgIV4OOyEkFlKFz","spotify:track:1Df1rxgMob1qQudexDEKuu","spotify:track:1HdNTlZrGTlgxDn31GB6Sv","spotify:track:1MOl6vGP299N8vd4zaHMTE","spotify:track:1srD2uc11TcQiOmHHrJp8M","spotify:track:1Wiv2h6vvSZyL1mFuVFfsY","spotify:track:2gmWJA9oF4GD2Vw5QoRqu1","spotify:track:2GrFTSvFN9I1PPN6y2Bjvl","spotify:track:2MJl8m9AbWgXLq4Ku7wWCX","spotify:track:3ApIYu95WxjzpQCnsLBbrv","spotify:track:3kpM8OxeMaaAWI9pErdj1S","spotify:track:3VZmChrnVW8JK6ano4gSED","spotify:track:4BNhasx75KbS10jHq3VZTz","spotify:track:4lqpGLAsSIrfqvM9zcxqhO","spotify:track:4sj8qFcEDnRPNv3tBbUVUf","spotify:track:4twhYPDyCP6ICeW3TtQVxP","spotify:track:6ABtlkvl08XQo6Xu24FJaf","spotify:track:6PTqC7OBPW5DwXPjd0sDEk","spotify:track:6Ycf7Ch2VlEKlORbz7yfpJ","spotify:track:7av4raprzW2bWdjyAaH3hz","spotify:track:13kCzuXquOJ9Un8piPp5X3","spotify:track:68WCHvnx4IPkzvgEyHXkGD"], "num": 500, "categories": ["I Want You","United","I Want You","Rapture","Capitol Gold: The Best Of Minnie Riperton","The Best Of The Gap Band","Thats The Way Of The World","Compositions","I Want You","Rhythm Of Love","Giving You The Best That I Got","Between the Sheets","Greatest Hits","Midnight Love","Thats The Way Of The World","Whats Going On - 40th Anniversary","360 Degrees Of Billy Paul","Capitol Gold: The Best Of Minnie Riperton","All This Love","Rapture","Rapture","Whats Going On - 40th Anniversary","Greatest Hits: Love TKO","Original Album Classics","spotify:album:28nUWsyczStUhYKXTY1IoW","spotify:album:67Eq3nfl1km9s5ig76Cc8B","spotify:album:0EM4Q0JUVZ8FNqmT5CI2E7","spotify:album:1C7VOpm96d77zf5yaRqJ2u","spotify:album:1Zc6fY5TjkirFsQIeX7KFL","spotify:album:3nsrmd93AcWiyVLtsWFbxL","spotify:album:5tXZfxvr2VaWibD74nw8VL","spotify:album:05WM21p9FQYRe1mbPJrCjf","spotify:album:28nUWsyczStUhYKXTY1IoW","spotify:album:1ehiOhlEIGDXl7XjkZH1Hi","spotify:album:2X4C9NBLaFtUSZLPqTC50W","spotify:album:35EP5dBkQWS0Lta6GE2VOu","spotify:album:0ynh84GggEZrLsImzquXs7","spotify:album:3gPlX9Zs3tXZZKNCyoOkSm","spotify:album:5tXZfxvr2VaWibD74nw8VL","spotify:album:3P9Pzn7O4Zsr3tsCSsx7Uk","spotify:album:3x36ONTtlbPuXrAjI3aNI6","spotify:album:1Zc6fY5TjkirFsQIeX7KFL","spotify:album:0idikg3MAbtPVfX7wwfBBW","spotify:album:1C7VOpm96d77zf5yaRqJ2u","spotify:album:1C7VOpm96d77zf5yaRqJ2u","spotify:album:4gp6F03qAJCvKYoAGSrHVk","spotify:album:0HDky3ocJvXf9UenxtOoc6","spotify:album:2mA0jZZC1qZLK0zIz5V6Bk","spotify:track:0gWmxML0Fc6z9e5adPqi1s","spotify:track:0JWeCKQU60BPmDkYFa9zN3","spotify:track:0m6i2lZNgIV4OOyEkFlKFz","spotify:track:1Df1rxgMob1qQudexDEKuu","spotify:track:1HdNTlZrGTlgxDn31GB6Sv","spotify:track:1MOl6vGP299N8vd4zaHMTE","spotify:track:1srD2uc11TcQiOmHHrJp8M","spotify:track:1Wiv2h6vvSZyL1mFuVFfsY","spotify:track:2gmWJA9oF4GD2Vw5QoRqu1","spotify:track:2GrFTSvFN9I1PPN6y2Bjvl","spotify:track:2MJl8m9AbWgXLq4Ku7wWCX","spotify:track:3ApIYu95WxjzpQCnsLBbrv","spotify:track:3kpM8OxeMaaAWI9pErdj1S","spotify:track:3VZmChrnVW8JK6ano4gSED","spotify:track:4BNhasx75KbS10jHq3VZTz","spotify:track:4lqpGLAsSIrfqvM9zcxqhO","spotify:track:4sj8qFcEDnRPNv3tBbUVUf","spotify:track:4twhYPDyCP6ICeW3TtQVxP","spotify:track:6ABtlkvl08XQo6Xu24FJaf","spotify:track:6PTqC7OBPW5DwXPjd0sDEk","spotify:track:6Ycf7Ch2VlEKlORbz7yfpJ","spotify:track:7av4raprzW2bWdjyAaH3hz","spotify:track:13kCzuXquOJ9Un8piPp5X3","spotify:track:68WCHvnx4IPkzvgEyHXkGD","Oldies","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:2i1IdHG5w0wiSmJGoqAGlj","spotify:artist:4TwHRCIu3Xg9fjS3l7owkp","spotify:artist:4QQgXkCYTt3BlENzhyNETg","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:53QzNeFpzAaXYnrDBbDrIp","spotify:artist:3DvdryKH4O95ZnsUZJKXpt","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:4QQgXkCYTt3BlENzhyNETg","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:187xgSpsFH8mMbAcoCW0zE","spotify:artist:2i1IdHG5w0wiSmJGoqAGlj","spotify:artist:6is2U7I1jlI8PjxNZOHIMV","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:46CH1Gp8l8QVly8bpG9JFG","spotify:artist:3koiLjNrgRTNbOwViDipeA","spotify:artist:68kACMx6A3D2BYiO056MeQ","spotify:artist:68kACMx6A3D2BYiO056MeQ","Marvin Gaye","Marvin Gaye","Marvin Gaye","Anita Baker","Minnie Riperton","The Gap Band","Earth, Wind & Fire","Anita Baker","Marvin Gaye","Anita Baker","Anita Baker","The Isley Brothers","Maze","Marvin Gaye","Earth, Wind & Fire","Marvin Gaye","Billy Paul","Minnie Riperton","DeBarge","Anita Baker","Anita Baker","Marvin Gaye","Teddy Pendergrass","Teddy Pendergrass","Soon Ill Be Loving You Again","Your Precious Love","After The Dance - Vocal","Caught Up In The Rapture","Inside My Love - Digitally Remastered 93","Outstanding - Original 12"" Mix","Reasons","Perfect Love Affair","I Want You","I Apologize","Good Love","Between the Sheets","Before I Let Go (feat. Frankie Beverly) [2004 - Remastered]","Sexual Healing","Thats the Way of the World","Save The Children","Me and Mrs. Jones","Lovin You - 1993 Digital Remaster","All This Love","Been So Long","Sweet Love","Whats Going On","Love TKO (Re-Recorded / Remastered)","Turn off the Lights"], "blackList": ["spotify:track:0gWmxML0Fc6z9e5adPqi1s","spotify:track:0JWeCKQU60BPmDkYFa9zN3","spotify:track:0m6i2lZNgIV4OOyEkFlKFz","spotify:track:1Df1rxgMob1qQudexDEKuu","spotify:track:1HdNTlZrGTlgxDn31GB6Sv","spotify:track:1MOl6vGP299N8vd4zaHMTE","spotify:track:1srD2uc11TcQiOmHHrJp8M","spotify:track:1Wiv2h6vvSZyL1mFuVFfsY","spotify:track:2gmWJA9oF4GD2Vw5QoRqu1","spotify:track:2GrFTSvFN9I1PPN6y2Bjvl","spotify:track:2MJl8m9AbWgXLq4Ku7wWCX","spotify:track:3ApIYu95WxjzpQCnsLBbrv","spotify:track:3kpM8OxeMaaAWI9pErdj1S","spotify:track:3VZmChrnVW8JK6ano4gSED","spotify:track:4BNhasx75KbS10jHq3VZTz","spotify:track:4lqpGLAsSIrfqvM9zcxqhO","spotify:track:4sj8qFcEDnRPNv3tBbUVUf","spotify:track:4twhYPDyCP6ICeW3TtQVxP","spotify:track:6ABtlkvl08XQo6Xu24FJaf","spotify:track:6PTqC7OBPW5DwXPjd0sDEk","spotify:track:6Ycf7Ch2VlEKlORbz7yfpJ","spotify:track:7av4raprzW2bWdjyAaH3hz","spotify:track:13kCzuXquOJ9Un8piPp5X3","spotify:track:68WCHvnx4IPkzvgEyHXkGD"]}'' \
http://localhost:8000/queries.json \

```
