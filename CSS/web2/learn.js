// first way to create a new empyu object

// var student = {
//     fisrtName: 'Ikromjon',
//     lastName: 'Khonaliev',
//     age: 20,
//     greeting: function(){
//         return "Hello I am " + this.fisrtName + " and I am " + this.age + " years old";
//     }
// };

// console.log(student.greeting());
// console.log(pupil.firstName);
// console.log(pupil.lastName);
// console.log(pupil.age);

// this is another way to create new object

// var student1 = new Guys();
// student1.fisrtName = "Islomjon";
// student1.lastName = "Khonaliev";
// student1.age = 23;

// // this is another way to create an object

// var student2 = {};
// student2.fisrtName = "Iftikhor";
// student2.lastName = "Khonaliev";
// student2.age = 17;


// sum.push(student);
// sum.push(student1);
// sum.push(student2);
// var sum = [];

// function Cars(carName, miles, year){
//     this.name = carName;
//     this.mile = miles;
//     this.productYear = year;
//     this.previewCars = function(){
//          return "Hello this is " + this.name + " car and its mile is " +
//          this.mile + " and these cars are producted in " + this.productYear;
//     };
// }

// var car1 = new Cars("BMW", 10, 2022);
// var car2 = new Cars("Mercedes", 12, 2021);
// var car3 = new Cars("Lambarghini", 15, 2022);
// var car4 = new Cars("AUDI", 13, 20021);

// sum.push(car1);
// sum.push(car2);
// sum.push(car3);
// sum.push(car4);

// for(var i = 0; i < sum.length; i++){
//     var car0 = sum[i];
//     console.log(car0.previewCars());
// }







// this is first way to create an object

// var Book1 = {
//     name: "Otkan Kunlar",
//     author: "Abdulla Qodiriy",
//     year: 1890,
//     about: function(){
//         return "This book is called " + this.name + " and the author is " +
//         this.author + " and this book was published first time in " + this.year;
//     }
// }

// console.log(Book1.name);
// console.log(Book1.author);
// console.log(Book1.year);
// console.log(Book1.about());

// this is second way

// var Book2 = new Object();
// Book2.name = "Mekhrobdan Chayon";
// Book2.author = "Abdulla Qodiriy";
// Book2.year = 1901;
// Book2.about = function(){return "This book is called " + this.name + " and the author is " +
// this.author + " and this book was published first time in " + this.year;
// }
// console.log(Book2.name);
// console.log(Book2.author);
// console.log(Book2.year);

// this one is the third way

// var Book3 = {};
// Book3.name = "Shaytanat";
// Book3.author = "Tokhir Malik";
// Book3.year = 2002;
// Book3.about = function(){return "This book is called " + this.name + " and the author is " +
// this.author + " and this book was published first time in " + this.year;
// }

// console.log(Book3.name);
// console.log(Book3.author);
// console.log(Book3.year);
// console.log(Book3.about());

// var total = [];
// total.push(Book1);
// total.push(Book2);
// total.push(Book3);

// for(var i = 0; i < total.length; i++){
//     var book = total[i];
//     console.log(book.about());
// }


// this one is the fourth way...

function Books(name,author,year){
    this.bookName = name;
    this.bookAuthor = author;
    this.bookYear = year;
}

var sums = [];
sums.push(new Books("O'tkan Kunlar", "Abdulla Qodiriy", 1890));
sums.push(new Books("Alvido Bolalik", "Tohir Malik", 2003));
sums.push(new Books("Shaytanat", "Tohir Malik", 2001));
sums.push(new Books("Ikki Eshik Orasi", "Erkin Vohidov", 2010));


// sums.push(Book1);
// sums.push(Book2);
// sums.push(Book3);
// sums.push(Book4);

for(var i = 0; i < sums.length; i++){
    console.log(sums[i]);
}