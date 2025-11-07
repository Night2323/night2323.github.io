var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write(s.length)

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write(s.toLowerCase())

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write(s.toUpperCase())

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
function WordCount(str) { 
return str.split(" ").length;
}
document.write(WordCount(s))

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write((s.split("e").length - 1)+(s.split("E").length - 1))

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write((s.split("az").length - 1))

var s = "Eljön még az idő, amikor a szellemi táplálék sokkal édesebb lesz Neked, mint bármiféle testi élvezet."
document.write(s.lastIndexOf('a'))