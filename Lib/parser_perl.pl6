use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> \; )* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) \= <Final> }
  rule Assgn { <Var> \= <Final> }
  rule Final { <Ite> | <Var> <FinalS> <Final> }
  rule FinalS { \u03a0 | \u03a3 }
  rule Ite { <Or> | <Or> \u2192 <Final> \u219b <Ite> }
  rule Or { <And> | <Or> \u2228 <And> }
  rule And { <SetE> | <And> \u2227 <SetE> }
  rule SetE { <SetC> <SetEH>* }
  rule SetEH { <SetES> <SetC> }
  rule SetES { \u2261 | \u2262 }
  rule SetC { <Union> <SetCH>* }
  rule SetCH { <SetCS> <Union> }
  rule SetCS { \u2282 | \u2283 | \u2286 | \u2287 | \u2208  }
  rule Union { <Int> | <Union> <UnionS> <Int> }
  rule UnionS { \\ | \u222a}
  rule Int { <NumE> | <Int> \u2229 <NumE> }
  rule NumE { <NumC> <NumEH>* }
  rule NumEH { <NumES> <NumC> }
  rule NumES { \u225f | \u2260 }
  rule NumC { <Add> <NumCH>* }
  rule NumCH { <NumCS> <Add> }
  rule NumCS { \< | \> | \u2264 | \u2265 }
  rule Add { <Mul> | <Mul> <AddS> <Mul> }
  rule AddS { \- | \+ }
  rule Mul { <Exp> | <Mul> <MulS> <Exp> }
  rule MulS { \u00d7 | \u00d8 | \% }
  rule Exp { <Unary> | <Unary> \^ <Exp> }
  rule Unary { <Atom> | <UnaryS> <Unary> }
  rule UnaryS { \~ | \u2214 | \u2238 | \u2201 | \u2110 | \u211b | \u220b | \u039c }
  rule Atom { <Number> | <Var> | <Finite> | <Infinite> | <Function> | <FunctionCall> | \( <Final> \) | \u2308 <Final> \u2309 | \[ <Final> \] | \u230a <Final> \u230b }
  rule FunctionCall { <Atom> \( <Final> (\,<Final>)* \) }
  rule Function { \( <FunctionHead> \u21a6 <Final> \) }
  rule FunctionHead { <Var> (\, <Var>)* (\, <Var> \u225d <Final>)* | <Var> \u225d <Final> (\, <Var> \u225d <Final>)* }
  rule Infinite { \{\:\} | \{ <Final> \: <Final> \} }
  rule Finite { \{\} | \{ <Final> (\, <Final>)* \} }
  token Var { <[A .. Z a .. z]> <[A .. Z a .. z 0 .. 9]>*}
  token Number { 0 | <[1 .. 9]> <[0 .. 9]>* }
  token ws { (\h | \s)* }
}
