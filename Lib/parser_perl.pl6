use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> \; )* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) \= <Final> }
  rule Assgn { <Var> \= <Final> }
  rule Final { <Ite> | <Var> <FinalS> <Final> }
  rule FinalS { \X03a0 | \X03a3 }
  rule Ite { <Or> | <Or> \X2192 <Final> \X219b <Ite> }
  rule Or { <And> | <Or> \X2228 <And> }
  rule And { <SetE> | <And> \X2227 <SetE> }
  rule SetE { <SetC> <SetEH>* }
  rule SetEH { <SetES> <SetC> }
  rule SetES { \X2261 | \X2262 }
  rule SetC { <Union> <SetCH>* }
  rule SetCH { <SetCS> <Union> }
  rule SetCS { \X2282 | \X2283 | \X2286 | \X2287 | \X2208  }
  rule Union { <Int> | <Union> <UnionS> <Int> }
  rule UnionS { \\ | \X222a}
  rule Int { <NumE> | <Int> \X2229 <NumE> }
  rule NumE { <NumC> <NumEH>* }
  rule NumEH { <NumES> <NumC> }
  rule NumES { \X225f | \X2260 }
  rule NumC { <Add> <NumCH>* }
  rule NumCH { <NumCS> <Add> }
  rule NumCS { \< | \> | \X2264 | \X2265 }
  rule Add { <Mul> | <Mul> <AddS> <Mul> }
  rule AddS { \- | \+ }
  rule Mul { <Exp> | <Mul> <MulS> <Exp> }
  rule MulS { \X00d7 | \X00d8 | \% }
  rule Exp { <Unary> | <Unary> \^ <Exp> }
  rule Unary { <Atom> | <UnaryS> <Unary> }
  rule UnaryS { \~ | \X2214 | \X2238 | \X2201 | \X2110 | \X211b | \X220b | \X039c }
  rule Atom { <Number> | <Var> | <Finite> | <Infinite> | <Function> | <FunctionCall> | \( <Final> \) | \X2308 <Final> \X2309 | \[ <Final> \] | \X230a <Final> \X230b }
  rule FunctionCall { <Atom> \( <Final> (\,<Final>)* \) }
  rule Function { \( <FunctionHead> \X21a6 <Final> \) }
  rule FunctionHead { <Var> (\, <Var>)* (\, <Var> \X225d <Final>)* | <Var> \X225d <Final> (\, <Var> \X225d <Final>)* }
  rule Infinite { \{\:\} | \{ <Final> \: <Final> \} }
  rule Finite { \{\} | \{ <Final> (\, <Final>)* \} }
  token Var { <[A .. Z a .. z]> <[A .. Z a .. z 0 .. 9]>*}
  token Number { 0 | <[1 .. 9]> <[0 .. 9]>* }
  token ws { (\h | \s)* }
}
