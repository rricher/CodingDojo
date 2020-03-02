<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>    
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Welcome</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>
<h1>New Product</h1>
<p>${errors}</p>
	<form method="post" action="/new">
        <p>
            <label for="name">Name</label>
            <input type="text" id="name" name="name"/>
        </p>
        <p>
            <label for="desc">Description</label>
            <input type="text" id="desc" name="desc"/>
        </p>
        <p>
            <label for="price">price</label>
            <input type="text" id="price" name="price"/>
        </p>
        <p>
            <label for="img">image link</label>
            <input type="text" id="img" name="img"/>
        </p>
        <p>Categories</p>
        <ul>
        	<c:forEach var="item" items="${categories}">
        		<li>${item.name}</li>
        	</c:forEach>
        </ul>
        <p>
            <label for="catg">or add one</label>
            <input type="text" id="catg" name="catg"/>
        </p>
        <input type="submit" value="create"/>
    </form>  
</body>
</html>