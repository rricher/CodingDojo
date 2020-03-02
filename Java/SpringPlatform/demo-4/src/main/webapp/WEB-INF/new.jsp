<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>    
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Registration Page</title>
</head>
<body>
    <div class="container"> 
    <h1>Add a show</h1>
    
    <p><form:errors path="show.*"/></p>
    
    <form:form method="POST" action="/new/show" modelAttribute="show">
        <p>
            <form:label path="title">Title</form:label>
            <form:input type="text" path="title"/>
        </p>
        <p>
            <form:label path="network">Network</form:label>
            <form:input type="text" path="network"/>
        </p>
        
        <input type="submit" value="Add"/>
    </form:form>
</div>

</body>
</html>