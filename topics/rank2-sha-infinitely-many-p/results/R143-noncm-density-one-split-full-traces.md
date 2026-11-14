# R143. 非 CM 的密度一分裂输入与同一完整非挠迹

日期：2026-11-12。**已证明；实际两步原始性仍开。**

[完整证明](../notes/2026-11-12-noncm-density-one-split-full-traces.md)。

固定 R136 的 \(E389\)、\(F=\mathbb Q(\sqrt{-7})\) 及原模参数化。
对任意固定 \(32/17<\eta<2\)，在 \(F\) 分裂的素数中存在相对
密度一的输入集合；每个充分大的输入 \(p\) 都有
\(\gg p^{\eta-1}/\log p\) 个 \(\ell\asymp p^\eta\) 满足
\[
 \begin{gathered}
 \ell\equiv-1\pmod{B_0p},\quad \ell+1=pu,\quad v_p(\ell+1)=1,\\
 a_p(E)\not\equiv0,\pm1\pmod p,\qquad
 a_\ell(E)\not\equiv0\pmod p,
 \end{gathered}
\]
其中 \(B_0\) 是 R140 预先固定的原 jet 进程模数。
同一选择的原完整迹 \(Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]\) 有
\[
 Q\text{ 非挠},\quad NQ=O,\quad
 v_\ell\log_E([t_0]Q)=1/p,\quad
 \widehat h(Q)\ll p^{2\eta-2}\log p=o(p^2),\quad
 Q\notin pE(F^{\rm ab}).
\]
而 R141 的 \(g_p\) 及实际全部 Hecke 总迹 \(a_\ell g_p\)
在两个固定负七 CM 源点都为简单零点。

证明先对 \(B_0p\) 应用 Fouvry/Mikawa 的平均等差下界。
由于 \(\ell+1<p^2\)，同一个候选 \(\ell\) 最多属于一个
\(p\in(X,2X]\)。原 jet 坏候选总数是 \(O(X^{2\eta-2})\)；
辅助位 \(a_\ell=0\) 则由 Elkies 的无条件零迹上界计为
\(O(X^{3\eta/4})\)。除以每个输入的候选下界后，损失的输入为
\[
 O\bigl(X^{\eta-1}\log X+X^{1-\eta/4}\log X\bigr)
                       =o(X/\log X).
\]
再同时删去 TZ 的普通/非异常例外与 R141 的 \(O(X^{3/4})\)
源退化例外，即得相对密度一；没有要求任意额外非阿贝尔
Chebotarev 条件，也没有对 \(a_p=\pm1\) 使用零迹的幂次界。

R139 的完整局部条件和 leading \(\delta Q\) 适用这些实际点，
但此处高度只为 \(o(p^2)\)，不保 R140 的 \(o(p)\) 或半长指数界。
仍须证明原纤维二阶矩无穷非零（或 \(a\le1\)）；源简单零与
完整非挠迹已经在同一密度一分裂集合上同时支付。
