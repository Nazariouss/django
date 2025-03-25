pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response contains success message", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.message).to.eql("User have been created");
});

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Token is returned", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.token).to.be.a("string");
});

pm.test("Unauthorized (401) without token", function () {
    pm.response.to.have.status(401);
    var jsonData = pm.response.json();
    pm.expect(jsonData.detail).to.include("Authentication credentials");
});

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is an array", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an("array");
});

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Contains logo and description", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.logo).to.be.a("string");
    pm.expect(jsonData.description).to.be.a("string");
});