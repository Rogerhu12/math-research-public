# R121. 密度一输入的实际完整迹与非零正局部化

日期：2026-11-12。**状态：已证明；主目标未完成。**

对固定 \(E:y^2=x^3-17x\)、\(F=\mathbb Q(\sqrt{-15})\)，任取
\(32/17<\theta<2\)。对同时在 \(F,\mathbb Q(i)\) 分裂的相对密度一输入素数 \(p\)，
可选择 R116 的同一个合法 \(\ell\ll p^\theta\)，使实际完整迹
\[
 Q_{p,\ell}=\operatorname{Tr}_U(1+\tau_3)P[\ell]\ne O,\qquad
 Q_{p,\ell}\notin pE(F[\ell])
\]
且首 jet 为单位，同时
\[
 \operatorname{im}\left(E(\mathbb Q)/p\longrightarrow
            E(\mathbb F_\ell)/p\right)\ne0.
\]
因此全局通常 Selmer 群在辅助位的正符号局部秩恰为 \(r_+=1\)。
R123 后可令辅助模数为显式 \(1020p\)。

证明使用两个固定独立点 \((-1,4),(9,24)\)。若两者约化都在
\(pE(\mathbb F_\ell)\)，这个群的阶为 \(u=(\ell+1)/p\)；
\(\sqrt u\) 尺度的二维盒子产生一个短的非零整线性组合，其分母被 \(\ell\) 整除。
全部 \(|a|,|b|\le\sqrt U+1\) 组合的分母乘积对数为 \(O(U^2)\)。
因此新增坏候选只有 \(O(U^2/\log X)\)，可与 R116 的实际 jet 坏集合一起删除，
仍留下密度一输入。限制—迹乘 \(2\) 保证该有理约化线在二次剩余域中不消失。

结论没有指定核线，没有给负符号局部化，也没有证明 \(Q\) 的 \(\delta\) 原始性。

完整证明：
[小辅助素数与两有理点的短关系](../notes/2026-11-12-small-auxiliary-primes-and-rational-localization.md)。

