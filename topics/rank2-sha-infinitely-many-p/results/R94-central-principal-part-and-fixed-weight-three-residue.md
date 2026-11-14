# R94. 实际中央行的整主部与固定权三留数解释

## 结论

对惰性 \(p\ge7\)，\(d=p+1\)，令
\[
\mathscr D=s\partial_t^2-8t\partial_t-1,\qquad
f_p=t^{-p-2}\left[\frac{M_eK^p}{sJ^{p+2}}\right]_{\le p+1}.
\]
实际四阶零点使 \(f_p\) 的极点阶只有 \(p-2\)，且系数全在
\(\mathbb Z_p\)。其水平留数准确为 \((C_d,0)\)，并唯一分解为
\[
f_p=\mathscr D(R_p)+C_d/t,\qquad
R_p\in t^{-1}\mathbb Z_p[t^{-2}],\quad
\operatorname{pole}(R_p)\le p-4.
\]
所有除数都是 \(m(m+1)\)、\(1\le m\le p-4\)，故没有隐藏的 \(p\) 损失。

取标准 \(\Theta=\vartheta_3^2\)、\(D_\tau=(2\pi i)^{-1}d/d\tau\)，
有 \(D_\tau t=s\Theta^2/8\)，以及准确的 Bol 恒等式
\[
\Theta D_\tau t\,f_p
=8D_\tau^2(R_p/\Theta)+C_d\,\Theta D_\tau t/t.
\]
在固定 \(\Gamma(2)\)、字符 \(\chi_4\) 上，直接尖点计算给
\(S_3(\Gamma(2),\chi_4)=0\)。固定 CM 内点的亚纯 Bol 商
因此由秩二纤维留数承载。几何基
\(\mathfrak c_0=[\omega\,dt/t]\)、\(\mathfrak c_1=[\omega\,dt/t^2]\)
的 Frobenius 为
\[
\Phi(\mathfrak c_0^\sigma)=p^2a_p\mathfrak c_1,\qquad
\Phi(\mathfrak c_1^\sigma)=pb_p\mathfrak c_0,\qquad \Phi^2=-p^3.
\]
指定饱和整类恰为
\[
p^{-1}[f_p\omega\,dt]=(C_d/p)\mathfrak c_0.
\]
因此它模 \(p\) 非零正好就是原来的首层充分条件，
不是额外的自动非零定理。

## 全局范围及深层成本

有限主部操作尚未证明与原 level \(68\) Hecke 关系交换。
实际完整权三提升在其他 CM 标记通常有 \(p+2\) 阶极点，
不能统一借用所选分支的四阶零点。
R96 在每个目标惰性 \(p\) 的特殊纤维上证明至少一半 CM 标记
的留数确实有一个 \(p\) 分母；完整形式的整格成本必须保留。
其唯一上升同源的极点还证明这个实际权三提升的几何 Hecke 像非零。

对每个 \(4\mid m\)，同一消元给实际
\[
f_m=\mathscr D(R_m)+C_m/t.
\]
若先给整输入，显式一般分母上界是 \((m-4)!\)。
当 \(m=(p+1)p^n,n\ge1\)，其估值为
\[
p^n+2(p^n-1)/(p-1)-n.
\]
输入周期还可能另有分母。固定秩二留数格及斜率 \(3/2\)
本身不提供这些随权变化主部的 Frobenius 迭代关系。

## 证明与校验

[全文](../notes/2026-11-12-central-principal-parts-pf-bol-residue.md)
逐项证明整消元、常数 \(8\)、尖点条件、几何规范和阶乘成本，
并与 R91 的真实 Hermite 中央行核对。
外部比较仅使用 Allen–Long–Saad 的明确留数序列及阶乘消灭结论。

[准确有理脚本](../scripts/check-central-pf-bol-residue.py)
从实际整数 theta 流恢复 \(M_e\)，根端完整复跑 \(p=7,11,19\)，
验证分解和全部整性，得到 \(C_d/p\bmod p=2,9,12\)。
主目标的跨素数非零性仍未证明。
