from bs4 import BeautifulSoup

sample_test = """<!doctype html>
<html class="no-js" lang="">

<head>
  <meta charset="utf-8">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title></title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <link rel="manifest" href="site.webmanifest">
  <link rel="apple-touch-icon" href="icon.png">
  <!-- Place favicon.ico in the root directory -->

  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/main.css">
</head>

<body>
  <!--[if lte IE 9]>
    <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
  <![endif]-->

  <!-- Add your site or application content here -->
  <p>Hello world! This is HTML5 Boilerplate.</p>
  <script src="something1">Something 1</script>
  <script src="something2">Something 2</script>
  <script>Nothing</script>
</body>

</html>"""

simple_soup = BeautifulSoup(sample_test,"html.parser")

def find_p():
	print(simple_soup.find('p').string)


def find_script():
  arr = [scr.string for scr in simple_soup.find_all('script') if "something2" not in scr.attrs.get('src',[])]
  print(arr)

def find_particular_script():
  print(simple_soup.find('script',{'src':'something1'}).string)


find_particular_script()