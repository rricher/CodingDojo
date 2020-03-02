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
    <h1>${show.title}</h1>
    <p>${show.network}</p>
    
    <table>
    <thead>
        <tr>
            <th>User</th>
            <th>Rating</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <c:forEach var="item" items="${show.ratings}">
            <tr>
                <td>${item.rater.email}</td>
                <td>${item.rate}</td>
                <c:if test="${item.rater.id == userid }">
                	<td><a href="/delete/rating/${item.id}/${show.id}">Delete</a></td>
               	</c:if>
            </tr>
        </c:forEach>
    </tbody>
</table>
	<p>${duplicate }</p>
    <p><form:errors path="rating.*"/></p>
    <form:form action="/rateshow/${show.id}" method="post" modelAttribute="rating">
        <p>
            <form:label path="rate">Rating</form:label>
            <form:input type="number" path="rate"/>
            <input type="submit" value="Rate!"/>
        </p>
    </form:form>
        
        
</div>

</body>
</html>