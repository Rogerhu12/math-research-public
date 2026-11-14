# R114：小 Heegner 辅助素数的真实迹与固定周期 jets

固定 R105 的 \(\Phi:X_0(3N_E)\to E_{17}\)，并令
\(\Psi=[2]\Phi\)。最大阶 CM 基点及其固定有限组共轭 \(c\)
均满足 \(\Psi(c)=O\)。在其固定 de Rham CM 本征基中取
\(v_c(0)=0,v_c'(0)=1\) 的 period 参数，定义固定代数系数
\[
\log_E\Psi(t_c(v))=\sum_{m\ge1}b_{c,m}v^m.
\]

令 \(\ell\) 在 \(F=\mathbb Q(\sqrt{-15})\) 和 \(\mathbb Q(i)\)
中均惰性，避开固定有限坏集，并设
\[
\ell+1=pu,\qquad u\ge3,
\qquad Q=\operatorname{Tr}_{U}X_\ell,
\qquad |U|=u.
\]
则全部 \(b_{c,ju}\)（\(1\le j\le p-1\)）在当前位整，而且
\[
\boxed{
\exists\,1\le j\le p-1:
b_{c,ju}\not\equiv0\pmod\ell
\quad\Longrightarrow\quad Q\ne O.}
\]

证明使用实际 canonical deformation 的 tame 商
\(\mathcal O_{F,\ell}^{\times}/\mathbb Z_\ell^{\times}\)。
其整平均线性化 \(w\) 与固定 period 参数满足
\(v_c=w+O(w^{\ell+2})\)。真实邻点为 \(w=r\)，
\(r^{\ell+1}=c_\ell\in\ell\mathcal O_B^\times\)。
若 \(\log_E\Psi(t(w))=\sum a_mw^m\)，则
\(m a_m\) 整、\(a_m=b_{c,m}\) 对 \(m\le\ell+1\)。
令 \(s=r^u\)，实际迹精确为
\[
\log_E([2]Q)
 =u\sum_{j=0}^{p-1}s^j
   \sum_{k\ge0}a_{u(j+kp)}c_\ell^k.
\]
尾项估值满足
\(k-v_\ell(j+kp)\ge1\)（\(k\ge1\)），故各基系数模
\(\ell\) 准确恢复上述固定低 jets，没有遗漏高阶同估值抵消。

R110 的密度一选择给 \(u\ge1020\)、\(u^2=o(\ell)\)。
后续 [R116](R116-density-one-nonzero-full-heegner-traces.md) 已用
固定普通 ST/Cornut 和跨素数乘积证明：对相对密度一输入，
可选实际首项 \(b_{c,u}\) 为单位，故真实迹非零且对数赋值为 \(1/p\)。
R110 随之给 \(Q\notin pE(H_\ell)\)，但这仍不等于
Kolyvagin 所需的增广底层原始性。
固定 \(v_c\) 是 period 参数，不能未经证明将此级数当作代数函数。

[完整证明、marking 与一手来源](../notes/2026-11-12-small-heegner-trace-and-cm-period-jets.md)
