# 🌐 URLs – Anatomy and Structure

A **URL (Uniform Resource Locator)** is the address of a resource on the web.
It tells the browser **where to go** and **how to fetch it**.


## General Structure of a URL

```
protocol://hostname:port/pathname?search#hash
```

![](/tutorial/img/url.png)

Let’s break it down:

### 🔹 Protocol

* Defines the **communication method** between browser and server.
* Common examples:

  * `http` → standard HyperText Transfer Protocol
  * `https` → secure HTTP (encrypted with SSL/TLS)
  * `ftp` → File Transfer Protocol

👉 Example: `https://`


### 🔹 Hostname / Domain

* Identifies the **server** where the resource is hosted.
* Examples:

  * `www.google.com`
  * `example.org`
  * Can also be an **IP address** like `192.168.1.1`


### 🔹 Port

* Specifies which **port** the server is listening on.
* Common defaults:

  * `80` for HTTP
  * `443` for HTTPS
* Often omitted when using the default.

👉 Example: `https://example.com:8080` → port `8080` is explicitly defined.


### 🔹 Pathname

* Points to the **specific resource** on the server.
* Example:

  * `/articles/python/`
  * `/images/logo.png`


### 🔹 Search (Query String)

* Provides **extra parameters** for the request.
* Starts with `?` and contains key-value pairs separated by `&`.

👉 Example:

```
https://example.com/search?q=django&page=2
```

* `q=django` → query parameter
* `page=2` → query parameter


### 🔹 Hash (Fragment)

* Identifies a **specific section** within the page.
* Starts with `#`.
* Handled by the browser (not sent to the server).

👉 Example:

```
https://example.com/docs#installation
```

This scrolls directly to the **Installation** section of the page.


### 🔹 href

It contains all the previous parts together.


## Example – Putting It All Together

```
https://www.example.com:443/products/item?id=10&ref=chatgpt#reviews
```

* **Protocol**: `https`
* **Hostname**: `www.example.com`
* **Port**: `443` (default for HTTPS)
* **Pathname**: `/products/item`
* **Search**: `?id=10&ref=chatgpt`
* **Hash**: `#reviews`

## URL cheatsheet

![](/tutorial/img/url-2.png)