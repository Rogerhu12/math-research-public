# R140. E389 在无穷大素因子上的真实非挠完整迹

日期：2026-11-12。状态：**已证明；二次增广原始性未证明。**

取 R136 的固定数据
\[
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}),\qquad
 \pi:X_0(389)\longrightarrow E,\quad \pi(\infty)=O.
\]
存在固定进程模数 \(B_0\)，使对充分大 \(x\)，有
\(\gg_{B_0}x/\log x\) 个实际辅助素数 \(\ell\le x\) 满足
\[
 \begin{gathered}
 \ell\equiv-1\pmod{B_0},\qquad
 p=P^+(\ell+1)>x^{667/1000},\qquad v_p(\ell+1)=1,\\
 a_p(E)\not\equiv0,\pm1\pmod p,\qquad
 a_\ell(E)\not\equiv0\pmod p.
 \end{gathered}
\]
写 \(\ell+1=pu\)，令 \(L/F\) 为 \(F[\ell]/F\) 的唯一次数
\(p\) 子扩张。则**同一组输入**的原完整迹
\[
                     Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]
\]
满足
\[
 \boxed{\quad
 Q\text{ 非挠},\qquad N_{L/F}Q=O,\qquad
 \widehat h(Q)\ll p^{666/667}\log p=o(p),\qquad
 Q\notin pE(F^{\rm ab}).
 \quad}
\]
这些候选至少给 \(\gg x^{667/1000}/\log x\) 个不同 \(p\)。
不要求 \(p\) 在 \(F\) 分裂。

证明包含四项不能由 R138 的筛选单独替代的输入：

1. 非 CM 挠点定理给固定
   \(t_0=\exp E(F^{\rm ab})_{\rm tors}\)。使用原固定映射
   \([t_0]\pi\)，两最大阶 \(389\)-Heegner 中心均映到 \(O\)。
   Silverman 的全阿贝尔域正高度下界对所有除点统一适用。
2. 固定 \(q=29\)、\(a_{29}=-6\)、\(29=N(1+2\sqrt{-7})\)。
   源 CM 的 ST/period 比较及 Cornut 的实际全 tame 迹定理，
   用整数 \(q-N\) 投影和准确的第二层 \(q-1=28\) 因子，
   证明指定 tame 指数 \(-1\) 的 Mellin 分支非恒零。
   因而存在固定 \(C=28\cdot29^k,m_0\)，使两中心的
   \(h_{c,m}=m!b_{c,m}\) 对 \(C\mid m,m\ge m_0\) 均非零。
3. 固定 \(B_0\) 为 \(C\) 的倍数且 \(B_0\ge m_0\)。
   每个大因子候选自动有 \(B_0\mid u\)。
   固定代数微分系统给非零整数 \(J_u\)，
   \(\log|J_u|\ll u\log u\)。全部坏候选 \(\ell\mid J_u\)
   的数量是 \(O(x^{666/1000})=o(x/\log x)\)，可与 R138
   的异常集合从同一个大素因子集合中同时删除。
4. R114 的源 CM 整线性化及完整对数尾界不要求目标 CM。
   对保留下来的实际点，
   \[
                         v_\ell\log_E([t_0]Q)=1/p,
   \]
   所以原全部迹确实非挠；再用
   \(\widehat h(Q)\le u^2\widehat h(P[\ell])\ll u^2\log\ell\)
   得到上述小高度和不可除性。

结合 R139，可将其 norm-one Euler 族及整 Selmer 上界用于这些
已证明非零的实际 \(Q\)。族的 leading 仍为 \(\delta Q\)，
不能删去一层 \(\delta\)。Gauss 整数算子只继续给
\(a\le(p-3)/2\)；这里没有证明 \(a\le1\) 或原半局部二阶矩非零。

[完整证明、初层递推及原始来源](../notes/2026-11-12-noncm-e389-nonzero-small-full-traces.md)。
全文已由另一代理独立审核，重点包括挠点各素数幂、两个 CM 中心、
固定 \(q=29\) 分支、固定进程量词及真实整乘积删除。
