use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> \; )* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) \= <Final> }
  rule Assgn { <Var> \= <Final> }
  rule Final { <Ite> | <Var> <FinalS> <Final> }
  rule FinalS { \x{03a0} | \x{03a3} }
  rule Ite { <Or> | <Or> \x{2192} <Final> \x{219b} <Ite> }
  rule Or { <And> | <Or> \x{2228} <And> }
  rule And { <SetE> | <And> \x{2227} <SetE> }
  rule SetE { <SetC> <SetEH>* }
  rule SetEH { <SetES> <SetC> }
  rule SetES { \u2261 | \u2262 }
  rule SetC { <Union> <SetCH>* }
  rule SetCH { <SetCS> <Union> }
  rule SetCS { \x{2282} | \x{2283} | \x{2286} | \x{2287} | \x{2208}  }
  rule Union { <Int> | <Union> <UnionS> <Int> }
  rule UnionS { \\ | \x{222a}}
  rule Int { <NumE> | <Int> \x{2229} <NumE> }
  rule NumE { <NumC> <NumEH>* }
  rule NumEH { <NumES> <NumC> }
  rule NumES { \x{225f} | \x{2260} }
  rule NumC { <Add> <NumCH>* }
  rule NumCH { <NumCS> <Add> }
  rule NumCS { \< | \> | \x{2264} | \x{2265} }
  rule Add { <Mul> | <Mul> <AddS> <Mul> }
  rule AddS { \- | \+ }
  rule Mul { <Exp> | <Mul> <MulS> <Exp> }
  rule MulS { \x{00d7} | \x{00d8} | \% }
  rule Exp { <Unary> | <Unary> \^ <Exp> }
  rule Unary { <Atom> | <UnaryS> <Unary> }
  rule UnaryS { \~ | \x{2214} | \x{2238} | \x{2201} | \x{2110} | \x{211b} | \x{220b} | \x{039c} }
  rule Atom { <Number> | <Var> | <Finite> | <Infinite> | <Function> | <FunctionCall> | \( <Final> \) | \x{2308} <Final> \x{2309} | \[ <Final> \] | \x{230a} <Final> \x{230b} }
  rule FunctionCall { <Atom> \( <Final> (\,<Final>)* \) }
  rule Function { \( <FunctionHead> \x{21a6} <Final> \) }
  rule FunctionHead { <Var> (\, <Var>)* (\, <Var> \x{225d} <Final>)* | <Var> \x{225d} <Final> (\, <Var> \x{225d} <Final>)* }
  rule Infinite { \{\:\} | \{ <Final> \: <Final> \} }
  rule Finite { \{\} | \{ <Final> (\, <Final>)* \} }
  token Var { <[A .. Z a .. z]> <[A .. Z a .. z 0 .. 9]>*}
  token Number { 0 | <[1 .. 9]> <[0 .. 9]>* }
  token ws { (\h | \s)* }
}
