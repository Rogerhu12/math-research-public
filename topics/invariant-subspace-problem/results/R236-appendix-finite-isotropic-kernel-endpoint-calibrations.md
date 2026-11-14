# R236 附录：全等向核子模上的有限位伪逆端项校准

日期：2026-11-13（UTC）。作者：central_review / Astra-ISP-0c017065；AI 辅助：GPT-6 Astra Pro。
状态：完整有限维恒等式；补充原两位真空校准。
四位全等向构造由 root 提出，central_review 独立逐项核验；root 已复读全部403行并核验两位与四位的完整配对。
本文不构造原无限 Haar 算子的核，也不反驳保留无限局部结构的排核方法。

## 1. 要检验的准确代入

全池背景估计已经控制
$$
T_0^k\prod_{j\in F}(L_j^{(0)})^{-2}.
$$
若想直接把原正交伪逆最高端项改写成这种带正次 $T_0$ 的乘积，
即使输入确在核内，也须另给证明。
下面的零背景模型说明：
仅凭 $T_0f=-Wf$、平方零多项式和全域 Leibniz 公式，
不能取得这种普遍因式化。

原两位校准计算的是参考真空；
本稿给一个真正属于有限模型核的输入。

## 2. 完整模型和配对

取
$$
H_2=\mathbb C^2\otimes\mathbb C^2,\qquad
Ee_0=e_1,\quad Ee_1=0,
$$
$$
E_1=E\otimes I,\qquad E_2=I\otimes E,
$$
并按 $00,01,10,11$ 排列基。
固定 $a,b>0$，令
$$
T=W=aE_1+bE_2,\qquad T_0=0,
$$
$$
C_2=E_1+E_2,\qquad
U=-\frac12(a^{-2}E_1^*+b^{-2}E_2^*),\qquad
V=C_2^\dagger.
\tag{2.1}
$$
设 $J$ 同时反射两位，定义原形式的双线性配对
$$
\mathcal B(x,y)=\langle x,J\overline y\rangle.
$$
对实向量，它是互补位的无共轭求和：
$$
\mathcal B(x,y)
=x_{00}y_{11}+x_{01}y_{10}+x_{10}y_{01}+x_{11}y_{00}.
\tag{2.2}
$$
各 $E_j$ 和 $T$ 对该配对对称。
这里不假设 $J$ 或相应反线性 $C$ 保持核。

由 $\operatorname{ad}_E^2(E^*)=-2E$，
$$
\operatorname{ad}_T^2U=C_2,
$$
所以
$$
[\operatorname{ad}_T^2U]V=P_{\operatorname{Ran}C_2}.
\tag{2.3}
$$
这是原有界正交范围投影。

## 3. 一个真正核向量

取
$$
f=b\,01-a\,10.
\tag{3.1}
$$
由于
$$
T\,01=a\,11,\qquad T\,10=b\,11,
$$
准确有
$$
Tf=0.
\tag{3.2}
$$
另外 $E_1f=b\,11$、$E_2f=-a\,11$，
所以此有限核本身也在两个纯位算子下不变。
这仍不是原无限算子的闭不变空间。

原正交伪逆满足
$$
V\,01=V\,10=\frac12\,00,
\qquad
V\,11=\frac12(01+10),\qquad V\,00=0.
$$
故
$$
Vf=\frac{b-a}{2}\,00.
$$
在核向量上，完整导子没有被简化错：
$$
(\operatorname{ad}_T^2V)f
=T^2Vf
=ab(b-a)\,11.
\tag{3.3}
$$
而
$$
U\,11=-\frac12(a^{-2}\,01+b^{-2}\,10).
$$
因此
$$
U(\operatorname{ad}_T^2V)f
=-\frac{ab(b-a)}2
(a^{-2}\,01+b^{-2}\,10).
\tag{3.4}
$$
代入 (2.2) 得
$$
\boxed{
\mathcal B\bigl(U(\operatorname{ad}_T^2V)f,f\bigr)
=\frac12(a-b)^2.
}
\tag{3.5}
$$
当 $a\ne b$ 时严格非零，而背景 $T_0$ 恒为零。

取 $\widehat f=f/\sqrt{a^2+b^2}$，更有
$$
\boxed{
\mathcal B\bigl(U(\operatorname{ad}_T^2V)\widehat f,\widehat f\bigr)
=\frac{(a-b)^2}{2(a^2+b^2)}.
}
\tag{3.6}
$$
共同缩放 $(a,b)\mapsto(\varepsilon a,\varepsilon b)$ 不改变这个值。
当 $a/b\to\infty$ 时，它趋于 $1/2$。
所以核约束本身也不把绝对小系数变成小端项。

## 4. 与全 Leibniz 完全一致

取局部测试 $D=I$。
原 $2r=2$ 的完整 Leibniz 配对仅留下最高右导子项，
故
$$
\mathcal B\bigl([\operatorname{ad}_T^2U]Vf,f\bigr)
=
\mathcal B\bigl(U(\operatorname{ad}_T^2V)f,f\bigr).
\tag{4.1}
$$
直接核验：
$$
P_{\operatorname{Ran}C_2}f
=\frac{b-a}{2}(01+10),
$$
所以
$$
\mathcal B(P_{\operatorname{Ran}C_2}f,f)
=\frac12(a-b)^2,
$$
与 (3.5) 一致。

因此非零端项不是遗漏了某个符号、闭域或额外 Leibniz 项；
它是保留原正交伪逆后的真实有限维行为。

## 5. 保留全 $C$ 等向的四位核子模

两位向量本身并非等向，因为
$\mathcal B(f,f)=-2ab$。
因此另给一个保持全等向子模的校准，
不把两位例子外推到原核已经满足的额外结构。

取
$$
H_4=(\mathbb C^2)^{\otimes4},\qquad E=e_{10},
$$
$$
T=E_1+2E_2+3E_3+4E_4,\qquad T_0=0,
$$
$$
C_4=\sum_{i=1}^4E_i,\qquad
U=-\frac12\sum_{i=1}^4 i^{-2}E_i^*,\qquad
V=C_4^\dagger,\qquad
P=C_4V.
\tag{5.1}
$$
仍取同时反射全部四位的原双线性配对 $\mathcal B_4$。
它把占据集 $F$ 配到补集 $F^c$。
全部算子全域有界，$T$ 对该配对对称。

这里提升深度为 $r=1$，位数为 $Q=4$，准确满足
$$
r<Q/2.
$$
全域恒等式仍为
$$
\operatorname{ad}_T^2U=C_4,\qquad
[\operatorname{ad}_T^2U]V=P_{\operatorname{Ran}C_4}.
\tag{5.2}
$$
使用 $2C_4/Q$ 的归一化时，只需相应缩放 $U,V$，
投影和以下配对值不变。

将二次占据层按
$$
12,\ 13,\ 14,\ 23,\ 24,\ 34
$$
排列。
取
$$
f_1=(0,3,-4,-6,8,0),\qquad
f_2=(2,0,-4,-6,0,12).
\tag{5.3}
$$
$T$ 从该层到 $123,124,134,234$ 层的矩阵为
$$
\begin{pmatrix}
3&2&0&1&0&0\\
4&0&2&0&1&0\\
0&4&3&0&0&1\\
0&0&0&4&3&2
\end{pmatrix}.
$$
逐项相乘得到
$$
Tf_1=Tf_2=0.
\tag{5.4}
$$

二次层的反射配对给
$$
\mathcal B_4(f_1,f_1)
=\mathcal B_4(f_2,f_2)=96,\qquad
\mathcal B_4(f_1,f_2)=48.
\tag{5.5}
$$
令
$$
\zeta=e^{2\pi i/3},\qquad f=f_1+\zeta f_2.
$$
由 $1+\zeta+\zeta^2=0$，
$$
Tf=0,\qquad
\mathcal B_4(f,f)=96(1+\zeta+\zeta^2)=0.
\tag{5.6}
$$
Hilbert 范数则是
$$
\|f_1\|^2=125,\quad \|f_2\|^2=200,\quad
\langle f_1,f_2\rangle=52,
$$
所以
$$
\boxed{\|f\|^2=273.}
\tag{5.7}
$$

现在取真正的纯位不变子模
$$
M=\operatorname{span}\{E_Ff:F\subset\{1,2,3,4\}\}.
\tag{5.8}
$$
各 $E_i$ 相互交换并与 $T$ 交换，故
$$
M\subset\ker T,\qquad E_iM\subset M.
$$
$M$ 的二次层只有 $f$ 的标量倍数，其余非零项都在三次或四次层。
反射配对只连接次数和为 $4$ 的层；
因此 (5.6) 已经给
$$
\boxed{\mathcal B_4(M,M)=0.}
\tag{5.9}
$$
这是真正全等向的整个子模，不只单个向量等向。
没有假设反线性 $C$ 保持 $M$。

## 6. 四位正交投影的准确核配对

二次层中的 $\operatorname{Ran}C_4$ 是从一次层得到的入射矩阵
$$
A=
\begin{pmatrix}
1&1&0&0\\
1&0&1&0\\
1&0&0&1\\
0&1&1&0\\
0&1&0&1\\
0&0&1&1
\end{pmatrix}
$$
的像，且
$$
A^{\mathsf T}A=2I+\mathbf1\mathbf1^{\mathsf T},
\qquad
(A^{\mathsf T}A)^{-1}
=\frac12I-\frac1{12}\mathbf1\mathbf1^{\mathsf T}.
\tag{6.1}
$$
故该层的实际正交投影是
$$
P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}.
$$

对二次层向量 $g,h$，记
$$
s_g=\sum_{\text{六条边}}g,\qquad y_g=A^{\mathsf T}g.
$$
补集反射满足
$$
A^{\mathsf T}Jh=s_h\mathbf1-y_h,
\qquad
\sum_i(y_g)_i=2s_g.
$$
由 (6.1) 直接得到
$$
\boxed{
\mathcal B_4(Pg,h)
=\frac23s_gs_h-\frac12y_g^{\mathsf T}y_h.
}
\tag{6.2}
$$

本例
$$
s_{f_1}=1,\qquad s_{f_2}=4,
$$
$$
y_{f_1}=(-1,2,-3,4),\qquad
y_{f_2}=(-2,-4,6,8).
$$
所以
$$
\left(\mathcal B_4(Pf_i,f_j)\right)_{i,j=1}^2
=
\begin{pmatrix}
-43/3&-4/3\\
-4/3&-148/3
\end{pmatrix}.
\tag{6.3}
$$
最终
$$
\begin{aligned}
\mathcal B_4(Pf,f)
&=-\frac{43}{3}-\frac83\zeta-\frac{148}{3}\zeta^2\\
&=35+\frac{140}{3}\zeta
=\boxed{\frac{35}{3}(1+2i\sqrt3)}\ne0.
\end{aligned}
\tag{6.4}
$$

由 $Tf=0$、$T$ 的 $\mathcal B_4$ 对称性及完整 $D=I$ Leibniz 等式，
$$
\boxed{
\mathcal B_4\bigl(U(\operatorname{ad}_T^2V)f,f\bigr)
=
\mathcal B_4(Pf,f)
=
\frac{35}{3}(1+2i\sqrt3).
}
\tag{6.5}
$$
对于 $\widehat f=f/\sqrt{273}$，该值除以 $273$。
共同缩放全部 $T$ 系数仍不改变归一配对值。

因此以下条件同时成立：

- 背景 $T_0=0$；
- $r<Q/2$；
- $M$ 在全部纯位 $E_i$ 下不变并包含于 $\ker T$；
- 整个 $M$ 对原位反射配对全等向；
- 原正交伪逆最高端项在 $M$ 上仍有非零配对。

关键是 $P$ 不保持这个等向子模。
不能从 $\mathcal B_4(M,M)=0$ 推出 $\mathcal B_4(PM,M)=0$。

## 7. 准确结论与边界

两位计算已经排除不保等向性的简单代入。
四位计算进一步排除以下无额外无限结构的代入：

> 在 $Tf=0$、$T=T_0+W$ 及全等向纯位不变子模中，
> 把原正交伪逆最高端项自动写成全部含正次 $T_0$ 的项，
> 随后套全池背景负项估计。

因为这里 $T_0=0$，但 (6.5) 仍非零。
该结论已经保留原反射配对和 $r<Q/2$；
不能通过指出两位旧例不等向来回避四位校准。

本例没有说明原无限 Haar 核存在。
有限模型仍缺少原 $A$ 的单射稠密限制、真实 carry、
无限高位强近似和实际局部不可约性等结构。
任何利用这些额外信息的排核方法仍须继续核验。
特别，不把有限子模 $M$ 称作原 $A$ 的不变子空间。

全池背景的共同预解和精确幅度乘积估计保持有效；
尚缺的是一个真正使用额外结构的连接，
而非仅移动 $T_0f=-Wf$ 穿过 $U,V$，或把全等向误写成局部等向。

来源：

- [原两位伪逆校准](../notes/2026-11-13-two-bit-pseudoinverse-calibration-central-next.md)。
- [全域双导子主稿](R236-appendix-global-bell-difference-units-and-double-commutator-projections.md)。
- [全池背景预解及精确乘积](../notes/2026-11-13-deleted-pool-bell-background-resolvents-and-exact-product-gain-central-review.md)。
