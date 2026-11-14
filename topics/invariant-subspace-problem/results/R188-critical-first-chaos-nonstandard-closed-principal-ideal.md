# R188：零锚有界第一 chaos 的非标准闭主理想

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整证明；R185 有限块机制的实际 Cayley 扩展。
本稿直接否定“所有非零第一 chaos 乘子都生成标准范数闭主理想”。原 $H$ 上该向量仍循环，不把范数理想问题与 ISP 混同。

## 1. 一个具体非负慢第一阶符号

固定
$$
a_j=(j+1)^{-2},\qquad M=\sum_ja_j\le2,
\qquad
Y_j=N_j(I+N_j)^{-1}.
$$
令
$$
\boxed{
S_1=\sum_{j\ge0}a_jY_j\in\mathcal A.
}
\tag{1.1}
$$
因为 $\|Y_j\|\le3$，该级数按算子范数绝对收敛。

R115 的不同位真实乘法给
$$
Y_j1=\frac{1-\chi_j}{2}.
$$
因此
$$
\boxed{
f=S_11
=\sum_{j\ge0}\frac{1-\chi_j}{2(j+1)^2}
=\frac M2-\frac12\sum_{j\ge0}\frac{\chi_j}{(j+1)^2}.
}
\tag{1.2}
$$
它是连续、有界、非负的第一 chaos，实际锚 $f(0)=0$。
所有系数正，所以 $f(y)=0$ 恰在全部物理位为0时，即 $y=0$；
因而 $f>0$ 几乎处处。

**主定理。** 对
$$
J_1=\overline{S_1\mathcal A}^{\|\cdot\|}
$$
有
$$
\boxed{
0\ne J_1\subsetneq I_1,\qquad
A^n\notin J_1\quad(n\ge0).
}
\tag{1.3}
$$
所以 $J_1$ 是无限余维的非标准闭主理想，不包含任何标准 $I_n$。
另一方面，原 $H$ 上 $S_1$ 单射、值域稠密，且 $f$ 循环。

证明使用 R174 的实际负整数边界，构造
$\ker\pi_-(S_1)$ 中的无限支持向量，且把 R185 所需的每个新误差单独核对。

## 2. 有限头仍有同一个 nilpotent 结构

在边界 $\mathscr H_-=\ell^2(\mathbb N_0)$ 上写
$$
\mathsf N_i=B^{2^i}/d_i,\qquad
\mathsf Y_i=\mathsf N_i(I+\mathsf N_i)^{-1},
\qquad
T_1=\pi_-(S_1)=\sum_i a_i\mathsf Y_i.
$$
沿用 R185 的纯孔消灭算子 $\mathsf E_i$、有限头
$\mathscr F_m$ 以及有限链 $\mathsf N_i^{[m]}$。

对实际和有限链都有
$$
\|\mathsf N_i\|,\ \|\mathsf N_i^{[m]}\|\le1,\qquad
\|\mathsf N_i^2\|,\ \|(\mathsf N_i^{[m]})^2\|\le\eta_i.
$$
由
$$
(I+X)^{-1}=(I-X)(I-X^2)^{-1}
$$
及 $\eta_i<1/4$，各逆的范数都小于3。

定义
$$
\mathsf Y_i^{[m]}
=\mathsf N_i^{[m]}(I+\mathsf N_i^{[m]})^{-1}.
$$
有限头对 $\mathsf N_i$ 不变，故逆的 Neumann 级数或有限多项式限制给
$$
T_1|_{\mathscr F_m}
=T_{1,m}:=\sum_{i<m}a_i\mathsf Y_i^{[m]},
\qquad
\|T_{1,m}\|\le3M\le6.
\tag{2.1}
$$
$i\ge m$ 的项在 $\mathscr F_m$ 上严格为零。

令 $d=2^m$。$T_{1,m}$ 是有限加权后移 $B_m$ 的无常数多项式，
最低项仍为 $(a_0/d_0)B_m$。所以
$$
\boxed{
T_{1,m}^d=0,\qquad
\ker T_{1,m}=\mathbb Ce_0.
}
\tag{2.2}
$$
Cayley 变换没有引入常数项或消去首个一次项。

## 3. 纯块纠错与更新后的放大常数

取 $m\ge2$、$d=2^m$、$L=64d$，
让间隔 $[m,L)$ 空置，在新块 $[L,2L)$ 使用 R185 §3 的
$$
D_{\mathcal B}=\sum_{i=L}^{2L-1}a_i\mathsf E_i.
$$
其逐次数右逆完全不变：
$$
D_{\mathcal B}h_k=h_{k-1},\qquad
h_0=\text{真空},\qquad
h_k\in\mathscr K_k,\qquad
\|h_k\|\le\delta^{-k},
$$
其中
$$
\delta=(32L^3)^{-1/2},\qquad 1\le k\le d-1.
$$
这些结论来自 R185 的自含交换子下界，未把实际 $\mathsf Y_i$ 当成纯算子。

对 $v\in\mathscr F_m$ 令
$$
V=\sum_{k=0}^{d-1}(-1)^kT_{1,m}^kv\otimes h_k.
\tag{3.1}
$$
由 (2.2) 和 $D_{\mathcal B}h_k=h_{k-1}$，
$$
(T_{1,m}\otimes I+I\otimes D_{\mathcal B})V=0.
\tag{3.2}
$$
若 $\varepsilon=\|T_{1,m}v\|$，则
$$
\|T_{1,m}^kv\|\le6^{k-1}\varepsilon\qquad(k\ge1).
$$
与 R185 同样的齐次数正交求和给
$$
\|V-v\|
\le\sqrt d\,\delta^{-1}(6\delta^{-1})^{d-2}\varepsilon.
$$
而 $\delta^{-1}<2^{12}d^{3/2}$，
所以 $6\delta^{-1}<2^{15}d^{3/2}$。对 $m\ge2$，
$$
(15+\tfrac32m)(\log2)\le8m.
$$
因此仍有
$$
\boxed{\|V-v\|\le e^{8m2^m}\|T_{1,m}v\|.}
\tag{3.3}
$$
每个修正项 $k\ge1$ 在新块有孔，故原低头系数精确保留。

## 4. 低位逆差必须保留空白间隔

记 $\mathscr U_{m,L}$ 为上述低头、空白间隔、新块组成的有限子空间。
本节核对真实
$$
T_1-(T_{1,m}\otimes I+I\otimes D_{\mathcal B})
$$
在整个 $\mathscr U_{m,L}$ 上的范数；不只检查某个模型向量。

### 4.1. 低位 $i<m$

使用不要求两算子交换的准确逆差恒等式：
$$
\mathsf Y_i-\mathsf Y_i^{[m]}
=(I+\mathsf N_i)^{-1}
(\mathsf N_i-\mathsf N_i^{[m]})
(I+\mathsf N_i^{[m]})^{-1}.
\tag{4.1}
$$
右边最后一个逆只作用低 $m$ 位，因而保持
$\mathscr U_{m,L}$，特别保持空白间隔。
R185 的真实 borrow 估计遂可用在中间差上：
$$
\|(\mathsf N_i-\mathsf N_i^{[m]})|_{\mathscr U_{m,L}}\|
\le\alpha_L/\alpha_i.
$$
两个逆的范数小于3，所以
$$
\boxed{
\|(\mathsf Y_i-\mathsf Y_i^{[m]})|_{\mathscr U_{m,L}}\|
\le9\alpha_L/\alpha_i.
}
\tag{4.2}
$$
不能只写全空间 $\eta_i$ 差；
(4.1) 中右逆的局部性正是保留远间隔收益的原因。

### 4.2. 空白间隔 $m\le i<L$

R185 给 $\|\mathsf N_i|_{\mathscr U_{m,L}}\|\le\alpha_L/\alpha_i$。
将逆放到左边，
$$
\mathsf Y_i=(I+\mathsf N_i)^{-1}\mathsf N_i,
$$
得到
$$
\boxed{\|\mathsf Y_i|_{\mathscr U_{m,L}}\|\le3\alpha_L/\alpha_i.}
\tag{4.3}
$$
不需要假设完整逆保持空白间隔。

### 4.3. 新块 $L\le i<2L$

由 $\mathsf N_i^2=\eta_i\mathsf N_{i+1}$，
$$
\mathsf Y_i-\mathsf N_i
=-\mathsf N_i^2(I+\mathsf N_i)^{-1}
$$
范数至多 $3\eta_i$。再加
$\|\mathsf N_i-\mathsf E_i\|\le\eta_i$，得
$$
\boxed{\|\mathsf Y_i-\mathsf E_i\|\le4\eta_i.}
\tag{4.4}
$$

$i\ge2L$ 时 $\mathsf N_i$ 严格杀掉 $\mathscr F_{2L}$，
其逆在这些输入上等于恒等，所以 $\mathsf Y_i$ 也严格杀掉。
没有遗漏更高实际尾。

将以上三类求和，并用 $\alpha_L/\alpha_i\le\eta_{L-1}$，
得到
$$
\boxed{
\|(T_1-T_{1,m}\otimes I-I\otimes D_{\mathcal B})|_{\mathscr U_{m,L}}\|
\le13M\eta_{L-1}\le26\eta_{L-1}.
}
\tag{4.5}
$$
因此模型核向量 (3.1) 满足
$$
\|T_1V\|\le26\eta_{L-1}\|V\|.
\tag{4.6}
$$

## 5. 同一个残差预算继续闭合

若
$$
\|v\|\le2,\qquad
\|T_1v\|\le e^{-40\,4^m},
$$
则 (2.1)、(3.3) 给
$$
\|V-v\|\le e^{-20\,4^m},\qquad \|V\|\le3.
$$
令 $m'=2L$，由 (4.6) 得
$$
\begin{aligned}
\|T_1V\|
&\le78\eta_{L-1}\\
&\le\exp\left(\log78-\frac{770}{16}\,4^{m'}\right)\\
&\le e^{-40\,4^{m'}}.
\end{aligned}
\tag{5.1}
$$
与 R185 相比常数从12变为78，但指数余量
$770/16-40=8.125$ 足够，且没有改变下一步的窗口定义。

## 6. 初始两孔向量的真实 Cayley 残差

仍取
$$
v_0=\frac{a_5e_{16}-a_4e_{32}}{\sqrt{a_4^2+a_5^2}},
\qquad m_0=6.
$$
纯和 $\sum_i a_i\mathsf E_i$ 杀掉它。

因为 $\mathsf E_i^2=0$，逆差给
$$
\mathsf Y_i-\mathsf E_i
=(I+\mathsf N_i)^{-1}
(\mathsf N_i-\mathsf E_i)(I-\mathsf E_i).
\tag{6.1}
$$
对每个单孔 $e_{2^j}$，
$$
(\mathsf N_i-\mathsf E_i)\mathsf E_i e_{2^j}=0:
$$
$i\ne j$ 时 $\mathsf E_ie_{2^j}=0$；
$i=j$ 时其像为 $e_0$，而实际和纯算子均杀掉 $e_0$。
所以 (6.1) 在这个向量上的右因子不会产生额外误差。

R185 的单孔公式遂给
$$
\|(\mathsf Y_i-\mathsf E_i)e_{2^j}\|
\le
\begin{cases}
3\alpha_j/\alpha_i,&i<j,\\
0,&i\ge j.
\end{cases}
$$
求和后
$$
\boxed{
\|T_1v_0\|
\le3M(\eta_3+\eta_4)
\le12\eta_3
<e^{-40\,4^6}.
}
\tag{6.2}
$$
实际指数仍为 $770\cdot16^3=3153920$，远大于预算的 $163840$。

## 7. 真实无限核与闭主理想

递归取
$$
m_{n+1}=128\,2^{m_n}
$$
并使用 (3.1) 的有限纠错。
(5.1) 保证残差预算，(3.3) 保证
$$
\sum_n\|v_{n+1}-v_n\|
\le\sum_ne^{-20\,4^{m_n}}<1/4.
$$
所以所有 $\|v_n\|<5/4$，满足每一步所需的 $\|v_n\|\le2$，
且强收敛到 $g_1$，满足
$$
T_1g_1=0.
$$
原 $e_{16}$、$e_{32}$ 系数始终保留，$e_0$ 系数始终为零。
故 $g_1\ne0$ 且 $g_1\perp e_0$。
由有限头 (2.2)，$g_1$ 不可能有有限支持，因此
$$
B^ng_1\ne0\qquad(n\ge0).
$$

连续边界表示给
$$
\pi_-(J_1)g_1=0.
$$
若某个 $A^n\in J_1$，便有 $B^ng_1=0$，矛盾。
这证明 (1.3)。

同 R185，$\ker T_1$ 是真无限维闭 $B$ 不变空间；
$J_1$ 无限余维，否则有限维商中的 $A+J_1$ 幂零，会迫某个幂属于 $J_1$。

R187 的全部商结构也逐项适用：唯一字符根理想各幂稠密；
连续有限维含幺表示只剩字符；
边界核的所有正次幂有同一个闭像，
并可删去至多一个根向量得到单射稠密的边界子商。
这些推论只需首阶1及不含任何幂，已在本稿验证。

## 8. 原第一阶向量仍循环，两个命题不可混淆

$f$ 是一个非零复 $\ell^2$ 第一 chaos（这里甚至实、非负、连续）。
R125 给其实际乘子 $S_1$ 在原 $H$ 上单射稠密，且 $f$ 循环。
也可直接用 R122：每个 dyadic gauge 只改变有限个 $Y_j$，
差是真解析函数，首项非零时为 $A$ 乘解析单位。

因此本稿同时给出
$$
\boxed{
f\text{ 在原 }H\text{ 上循环},\qquad
\overline{X_f\mathcal A}^{\|\cdot\|}
\text{ 非标准且不含任何 }A^n.
}
$$

R116/R118 的快系数标准理想定理不能删去衰减条件，
并替换为仅有第一 chaos 或 $\ell^1$ 系数。
本例直接位于此前未判定的零锚慢第一阶类别。

这不否定 R125 的第一阶循环性，
不构造原 Haar 空间上的非零核，也不绕开 R174/R187 的归一化幂传输障碍。
完整 Hilbert 不变子空间问题仍然开放。
