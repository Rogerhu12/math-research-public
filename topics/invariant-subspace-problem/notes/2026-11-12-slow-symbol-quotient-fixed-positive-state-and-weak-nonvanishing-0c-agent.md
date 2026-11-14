# R210：慢符号商中的固定正湮灭态与归一化幂的弱非消失

日期：2026-11-12（UTC）。作者：literature；l2_moments 独立核验了短块追加与弱首步修复接口。
状态：完整证明。本文处理两个实际范数闭主理想，构造同一个固定对偶泛函在无限子列上的非消失；不是一列随指标变化的泛函。

## 1. 主结论与范围

在原 Haar 表示中记
$$
\mathfrak U=\text{实际 UHF 代数},\qquad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}\subset\mathfrak U,
$$
$$
N_j=A^{2^j}/d_j,\qquad
Y_j=N_j(I+N_j)^{-1},\qquad
a_j=(j+1)^{-2}.
$$
定义
$$
S_N=\sum_{j\ge0}a_jN_j,\qquad
S_Y=\sum_{j\ge0}a_jY_j,
$$
以及
$$
J_\bullet=\overline{S_\bullet\mathcal A}^{\|\cdot\|},
\qquad
q_\bullet:\mathcal A\longrightarrow\mathcal A/J_\bullet
\quad(\bullet=N,Y).
\tag{1.1}
$$
两个级数都按算子范数绝对收敛。

**定理。** 对每一个 $\bullet=N,Y$，分别存在严格递增的整数序列
$j_k$ 和 $\mathfrak U$ 的一个固定正状态 $\varphi_\bullet$，满足
$$
\varphi_\bullet(J_\bullet)=0,\qquad
\varphi_\bullet(I)=1,
\tag{1.2}
$$
以及
$$
\boxed{
\lim_{k\to\infty}\varphi_\bullet(N_{j_k})
=
\lim_{k\to\infty}\varphi_\bullet(Y_{j_k})
=\frac{\sqrt3}{4}.
}
\tag{1.3}
$$
两个模型可以有不同的选位序列和不同的状态；没有宣称一个状态同时湮灭两个理想。

因此 $q_\bullet(N_j)$ 与 $q_\bullet(Y_j)$ 都不在 Banach 商的弱拓扑
$\sigma(\mathcal A/J_\bullet,(\mathcal A/J_\bullet)^*)$ 中趋于零。

$\varphi_\bullet|_{\mathcal A}$ 不能由原 Haar 表示中的任何正常泛函表示；
它也不能由负整数边界表示中的正常泛函表示。
前者在 $N_j$ 上的极限必须是 $1/2$，后者必须是0，而 (1.3) 位于两者之间。

所以本文关闭的是“整个 Banach 商对偶使 $q(N_j)$ 弱趋零”这一充分条件候选。
它没有构造 Haar 正常湮灭态，没有否定
$I\in\overline{S_\bullet\mathcal A}^{\mathrm{SOT}}$，
也没有解决 $S_\bullet$ 在原 Haar 不变限制上的值域稠密性。

## 2. 使用的实际边界与有限块输入

R174 给出 $\mathfrak U$ 的含幺等距 $*$ 表示
$$
\pi_-:\mathfrak U\longrightarrow B(\mathscr H_-),
\qquad
\mathscr H_-=\ell^2(\mathbb N_0).
$$
基向量 $e_n$ 表示相对物理全1参考态的有限孔配置。
记
$$
B=\pi_-(A),\qquad
\mathsf N_j=\pi_-(N_j),\qquad
\mathsf Y_j=\pi_-(Y_j).
$$
纯孔消灭算子为
$$
\mathsf E_je_n=
\begin{cases}
e_{n-2^j},&n_j=1,\\
0,&n_j=0.
\end{cases}
$$
实际递推是
$$
\mathsf N_j=\mathsf E_j+\eta_j\mathsf E_j^*\mathsf N_{j+1},
\qquad
\mathsf N_j^2=\eta_j\mathsf N_{j+1},
$$
$$
\|\mathsf N_j\|=1,\qquad
0<\eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j}.
\tag{2.1}
$$
于是
$$
\|\mathsf N_j-\mathsf E_j\|\le\eta_j,\qquad
\|\mathsf Y_j-\mathsf E_j\|\le4\eta_j,\qquad
\|\mathsf Y_j-\mathsf N_j\|\le3\eta_j.
\tag{2.2}
$$

以下固定两个模型之一，并统一记
$$
T=\pi_-(S_\bullet),\qquad
M=\sum_ja_j\le2.
$$
两种情形均有 $\|T\|\le6$。
设
$$
\mathscr F_m=\operatorname{span}\{e_n:0\le n<2^m\},
\qquad P_m^-:\mathscr H_-\to\mathscr F_m.
$$
这是边界的有限头投影，不是原 Haar 有限柱投影。

有限头对 $T$ 不变，而且
$$
T_m=T|_{\mathscr F_m},\qquad
\|T_m\|\le6,\qquad
T_m^{2^m}=0.
\tag{2.3}
$$
$N$ 模型的 $\|T_m\|\le2$，但全文使用统一常数6。

R185 §§3–6 与 R188 §§3–5 已自含证明如下有限块修复。
对 $h\ge2$，令
$$
L_h=64\,2^h,\qquad H_h=2L_h=128\,2^h.
$$
存在一个明确的有限维线性映射
$$
\mathcal R_h:\mathscr F_h\longrightarrow\mathscr F_{H_h}
$$
使对每个 $y\in\mathscr F_h$，
$$
\boxed{
\|\mathcal R_hy-y\|
\le e^{8h2^h}\|Ty\|,
}
\tag{2.4}
$$
$$
\boxed{
\|T\mathcal R_hy\|
\le26\,\eta_{L_h-1}\|\mathcal R_hy\|.
}
\tag{2.5}
$$
修正项的全部整数支持指标至少为 $2^{L_h}$，故低头系数精确保留。

为明确这个输入，令
$D=\sum_{i=L_h}^{2L_h-1}a_i\mathsf E_i$。
块内按孔数分层，纯创建的交换子给
$$
\|D^*v\|^2\ge(32L_h^3)^{-1}\|v\|^2
\quad\text{在孔数不超过 }2^h\text{ 的层上}.
$$
故可选有限向量 $u_0=\Omega,u_1,\ldots,u_{2^h-1}$，使
$$
Du_k=u_{k-1},\qquad
\|u_k\|\le(32L_h^3)^{k/2}.
$$
实际修复公式是
$$
\mathcal R_hy
=\sum_{k=0}^{2^h-1}(-1)^kT_h^ky\otimes u_k,
\tag{2.6}
$$
中间坐标 $[h,L_h)$ 全部取无孔真空。
模型 $T_h\otimes I+I\otimes D$ 精确杀掉此向量。
齐次数正交求和给 (2.4)；真实 borrow 必须跨空白间隔，
给 (2.5)。Cayley 情形两个低头逆各付范数3，
正是常数26的来源。这里不替换原实际算子。

## 3. 可反复使用的精确核向量类

称单位向量 $g\in\ker T$ 为可递归近似的，如果存在趋于无穷的头窗口 $m_n$，
使
$$
v_n=P_{m_n}^-g,\qquad
\|g-v_n\|\le4e^{-20\,4^{m_n}},
\qquad
\|Tv_n\|\le2e^{-40\,4^{m_n}}.
\tag{3.1}
$$
只要求沿这些窗口成立，不要求对每个整数 $m$ 都有同一估计。

真空 $e_0$ 属于此类：$Te_0=0$，而任何有限头投影都固定它。
下一个引理说明，任意足够小残差的有限头单位向量都可修复进这个类。
关键是不要求初始向量已经满足新头窗口的 $40$ 指数预算。

**弱首步修复引理。**
给定 $0<\delta<1/4$，设 $y\in\mathscr F_h$ 为单位向量，并满足
$$
e^{8h2^h}\|Ty\|\le\delta/4,\qquad
2e^{-20\,4^{H_h}}\le\delta/4.
\tag{3.2}
$$
当 $h$ 足够大时，存在满足 (3.1) 的单位向量
$g\in\ker T$，且
$$
\boxed{\|g-y\|\le\delta.}
\tag{3.3}
$$

**证明。**
先只用有限公式 (2.6)，置 $V=\mathcal R_hy$。
由 (2.4)，
$$
\|V-y\|\le\delta/4,\qquad \|V\|\le9/8.
$$
由 (2.5) 和
$16^{L_h-1}=4^{H_h}/16$，
$$
\|TV\|
\le(26\cdot9/8)\exp\left(-\frac{770}{16}4^{H_h}\right)
\le e^{-40\,4^{H_h}}
\tag{3.4}
$$
对全部足够大的 $h$ 成立。
因此从窗口 $H_h$ 开始，R185/R188 的标准递归预算才首次启动。

标准递归每步将窗口 $m$ 换为 $128\,2^m$，
移动至多 $e^{-20\,4^m}$，并保持残差不超过
$e^{-40\,4^m}$。
所有后续位移之和不超过
$2e^{-20\,4^{H_h}}$。
这既保持迭代向量范数小于2，又给精确核极限 $G$：
$$
TG=0,\qquad
\|G-y\|
\le\delta/4+2e^{-20\,4^{H_h}}
\le\delta/2.
$$
故 $\|G\|\ge1-\delta/2>7/8$。令 $g=G/\|G\|$，
则
$$
\|g-y\|\le2\|G-y\|\le\delta.
$$

所有后续修正都严格位于当次旧头之外，所以每个迭代有限向量
正是 $G$ 在相应窗口上的投影。
余下位移之和至多 $2e^{-20\,4^m}$。
除以 $\|G\|>7/8$ 后，尾误差小于
$4e^{-20\,4^m}$，残差小于
$2e^{-40\,4^m}$。
所以单位向量 $g$ 满足 (3.1)。证毕。

## 4. 四位短块中的纯核相干向量

取 $j\ge32$，使用四位块
$$
\mathcal B_j=\{j,j+1,j+2,j+3\}.
$$
本节的 $e_{2^k}$ 只表示这个局部块中的单孔向量，其余块坐标无孔。
令
$$
\sigma_j^2=\sum_{k=j+1}^{j+3}a_k^2,
$$
$$
u_j=
\frac{
\sigma_je_{2^j}
-(a_j/\sigma_j)\sum_{k=j+1}^{j+3}a_ke_{2^k}
}
{\sqrt{\sigma_j^2+a_j^2}}.
\tag{4.1}
$$
直接计算得到
$$
\|u_j\|=1,\qquad
\left(\sum_{k=j}^{j+3}a_k\mathsf E_k\right)u_j=0.
$$
又令
$$
\psi_j=\frac{\Omega+u_j}{\sqrt2},\qquad
c_j=\frac{\sigma_j}{\sqrt{\sigma_j^2+a_j^2}}.
\tag{4.2}
$$
纯块和也杀掉 $\Omega$，所以
$$
\|\psi_j\|=1,\qquad
D_j\psi_j=0,\qquad
D_j=\sum_{k=j}^{j+3}a_k\mathsf E_k.
\tag{4.3}
$$
选定位 $j$ 的孔消灭期望为
$$
\boxed{\langle\mathsf E_j\psi_j,\psi_j\rangle=c_j/2.}
\tag{4.4}
$$

由于
$$
\frac{\sigma_j^2}{a_j^2}
=\sum_{r=1}^{3}\left(\frac{j+1}{j+r+1}\right)^4
\longrightarrow3,
$$
有
$$
\frac{c_j}{2}\longrightarrow\frac{\sqrt3}{4}.
\tag{4.5}
$$
当 $j\ge32$ 时，
$$
2<
3(11/12)^4
\le\frac{\sigma_j^2}{a_j^2}<3,
$$
从而可使用简单统一区间
$$
\boxed{\frac25<\frac{c_j}{2}<\frac{11}{25}<\frac12.}
\tag{4.6}
$$
这里使用的不是近似核：纯块零等式 (4.3) 完全精确。

## 5. 给旧核向量追加短块：全部实际误差

设 $g$ 是 (3.1) 的可递归近似单位核向量。
选它的一个足够深窗口 $m$，置
$$
v=P_m^-g,\qquad
\widehat v=v/\|v\|,\qquad
j=m+1,\qquad h=m+5.
$$
$m$ 大时 $\|v\|\ge1/2$。
在旧头 $[0,m)$ 后留一个无孔间隔位 $m$，
然后添加四位块 $[m+1,m+5)$，其后仍无孔。
定义有限头单位向量
$$
y=\widehat v\otimes\Omega_{\{m\}}\otimes\psi_j
\in\mathscr F_h.
\tag{5.1}
$$

### 5.1. 模型残差

模型算子为 $T_m\otimes I+I\otimes D_j$。
由 (4.3)，它在 $y$ 上的像只有旧残差：
$$
\|(T_m\otimes I+I\otimes D_j)y\|
=\frac{\|Tv\|}{\|v\|}
\le4e^{-40\,4^m}.
\tag{5.2}
$$

### 5.2. $N$ 模型的真实 borrow

对 $i<m$，将递推 (2.1) 展开到 $j=m+1$。
第 $m$ 位无孔，因此中间在该位消灭的项为零，
而未被旧有限头包含的有效 carry 满足
$$
\|(\mathsf N_i-\mathsf N_i^{[m]})y\|
\le\alpha_j/\alpha_i\le\eta_m.
\tag{5.3}
$$
同一估计对整个旧头、无孔间隔、新块所组成的有限子空间统一成立。

对间隔位 $i=m$，亦有
$\|\mathsf N_my\|\le\eta_m$。
对四个新块位，用
$\|\mathsf N_i-\mathsf E_i\|\le\eta_i\le\eta_m$。
对 $i\ge h$，$\mathsf N_i$ 严格杀掉 $\mathscr F_h$。
总误差不超过 $4\eta_m$。

### 5.3. $Y$ 模型的两个逆

低位使用准确逆差恒等式
$$
\mathsf Y_i-\mathsf Y_i^{[m]}
=(I+\mathsf N_i)^{-1}
(\mathsf N_i-\mathsf N_i^{[m]})
(I+\mathsf N_i^{[m]})^{-1}.
\tag{5.4}
$$
右侧最后一个逆只作用旧头，保持间隔位无孔；
两个逆的范数均不超过3。
因此低位差不超过 $9\alpha_j/\alpha_i$。
间隔位用
$\mathsf Y_m=(I+\mathsf N_m)^{-1}\mathsf N_m$，
付常数3。
新块位用 (2.2)，付常数4。
块后项仍严格为零。

沿 R188 的同一求和，两个模型统一满足
$$
\boxed{
\|Ty\|
\le r_m:=4e^{-40\,4^m}+26\eta_m.
}
\tag{5.5}
$$

### 5.4. 为什么新的首步成本始终可支付

新窗口是 $h=m+5$，而非旧 $m$。
这里只需检查
$$
e^{8h2^h}r_m\longrightarrow0.
\tag{5.6}
$$
这是因为
$$
8(m+5)2^{m+5}=o(4^m),\qquad
\eta_m\le e^{-770\,16^m}.
$$
所以给定任意 $\delta>0$，可在 (3.1) 的窗口序列上取 $m$
充分大，使弱首步修复引理适用，
得到新的可递归近似单位核向量 $g'$，满足
$$
\boxed{\|g'-y\|\le\delta.}
\tag{5.7}
$$
没有把旧 $e^{-40\,4^m}$ 误当成新窗口所需的
$e^{-40\,4^{m+5}}$。恰是 §3 的弱首步修复避开了这个错误。

## 6. 旧选定位期望的保持与新选定位期望

记
$$
\tau_m=\|g-P_m^-g\|.
$$
当 $\tau_m<1/2$ 时，
$$
\|\widehat v-g\|\le2\tau_m.
\tag{6.1}
$$
对单位向量 $x,z$ 及收缩算子 $R$，
$$
|\langle Rx,x\rangle-\langle Rz,z\rangle|
\le2\|x-z\|.
\tag{6.2}
$$

固定任意旧位 $i<m$。在旧向量 $\widehat v$ 上，
$\mathsf N_i$ 的有限头限制恰为 $\mathsf N_i^{[m]}$。
在新张量 $y$ 上，(5.3) 给差至多 $\eta_m$。
$\mathsf N_i^{[m]}$ 只作用旧头，其期望因追加单位张量因子而保持。
结合 (6.1)、(6.2)、(5.7)，
$$
\boxed{
|\langle\mathsf N_ig',g'\rangle
-\langle\mathsf N_ig,g\rangle|
\le4\tau_m+\eta_m+2\delta.
}
\tag{6.3}
$$
该界对全部旧位 $i<m$ 同时成立。

对新选定位 $j=m+1$，低头与其完全分离。
由 (2.2)、(4.4)、(5.7)，
$$
\boxed{
|\langle\mathsf N_jg',g'\rangle-c_j/2|
\le\eta_j+2\delta.
}
\tag{6.4}
$$
这两条估计已经包含真实进位、旧头截断、局部张量添加以及最后的规范化；
不需要假设无限向量乘积收敛。

## 7. 无限追加：只取状态聚点，不取向量强极限

令
$$
\delta_s=2^{-s-10}\qquad(s\ge1),
$$
从 $g_0=e_0$ 开始。
归纳假设 $g_{s-1}$ 是可递归近似单位核向量，
且已选了 $j_1<\cdots<j_{s-1}$。

在它的 (3.1) 窗口序列中取 $m_s$ 充分大，满足：

- $m_s>j_{s-1}+3$，且 $m_s\ge32$；
- $\tau_{m_s}\le\delta_s$、$\eta_{m_s}\le\delta_s$；
- §3 的两条预算对 $h=m_s+5$、$\delta=\delta_s$ 成立。

这些都是关于 $m_s$ 足够大的条件，由 (3.1)、(5.6) 可同时满足。
置 $j_s=m_s+1$，按 §§5–6 得到新的单位向量 $g_s\in\ker T$。

由 (6.3)，对任何 $k<s$，
$$
|\langle\mathsf N_{j_k}g_s,g_s\rangle
-\langle\mathsf N_{j_k}g_{s-1},g_{s-1}\rangle|
\le7\delta_s.
\tag{7.1}
$$
由 (6.4)，
$$
|\langle\mathsf N_{j_s}g_s,g_s\rangle-c_{j_s}/2|
\le3\delta_s.
\tag{7.2}
$$
因此对全部 $r\ge k$，
$$
\boxed{
|\langle\mathsf N_{j_k}g_r,g_r\rangle-c_{j_k}/2|
\le3\delta_k+7\sum_{s=k+1}^{r}\delta_s
\le10\delta_k.
}
\tag{7.3}
$$

每一步添加一个有固定非真空质量的局部 $\psi_j$。
本证明没有、也不需要声称 $g_s$ 范数收敛。
可和的是每次真实修复误差及每个旧选定位期望的后续变化，
不是向量本身每一步的总位移。

## 8. 一个固定的 UHF 正湮灭态

在实际 UHF 代数上定义单位向量状态
$$
\varphi_r(E)=\langle\pi_-(E)g_r,g_r\rangle
\qquad(E\in\mathfrak U).
\tag{8.1}
$$
因为 $\pi_-$ 是含幺 $*$ 表示，$\varphi_r$ 确实是正状态。
因为 $Tg_r=0$，且 $\pi_-(F)$ 与 $T$ 交换，
对每个 $F\in\mathcal A$，
$$
\varphi_r(S_\bullet F)
=\langle T\pi_-(F)g_r,g_r\rangle=0.
\tag{8.2}
$$
由范数连续性，
$$
\varphi_r(J_\bullet)=0.
\tag{8.3}
$$

UHF 状态空间弱*紧。取沿 $r\to\infty$ 的任意弱*聚点 $\varphi$。
也可利用 $\mathfrak U$ 可分，在其状态空间中取收敛子序列。
它仍是正状态，$\varphi(I)=1$，且 (8.3) 对每个固定理想元素保留：
$$
\varphi(J_\bullet)=0.
\tag{8.4}
$$

现在固定 $k$ 后令 $r$ 沿这个子网或子序列趋于无穷。
(7.3) 给
$$
\boxed{
|\varphi(N_{j_k})-c_{j_k}/2|\le10\delta_k.
}
\tag{8.5}
$$
最后才令 $k\to\infty$。
由 $j_k\to\infty$、(4.5) 和 $\delta_k\to0$，
得到
$$
\lim_{k\to\infty}\varphi(N_{j_k})=\sqrt3/4.
$$
再用
$\|Y_j-N_j\|\le3\eta_j$，便得同样的 $Y_{j_k}$ 极限。

若需要统一正下界，(4.6)、(8.5) 与
$10\delta_1=5/1024<1/128$ 给
$$
\frac38<\Re\varphi(N_{j_k})<\frac{15}{32}
\qquad(k\ge1).
\tag{8.6}
$$
这是一个已经固定的状态对全部选定位同时成立的界，
不是给每个 $j_k$ 另选一个状态。

## 9. Banach 商弱零候选被实际否定

$\varphi|_{\mathcal A}$ 是范数1的连续线性泛函，并湮灭闭理想
$J_\bullet$。
因此它下降为商上的连续线性泛函
$$
\overline\varphi:\mathcal A/J_\bullet\longrightarrow\mathbb C,
\qquad
\overline\varphi(q_\bullet(F))=\varphi(F).
$$
由于 $\overline\varphi(q_\bullet(I))=1$，其范数仍为1。
式 (1.3) 现在直接给
$$
\overline\varphi(q_\bullet(N_{j_k}))\longrightarrow\sqrt3/4\ne0.
$$
所以
$$
\boxed{q_\bullet(N_j)\not\rightharpoonup0.}
\tag{9.1}
$$
同理 $q_\bullet(Y_j)\not\rightharpoonup0$。

只知道某些随 $j$ 变化的单位态
$\varphi_j(N_j)\to1/2$，本来只能得到商范数不趋零，
不能推出 (9.1)。
§§5–8 的反复短块追加与固定状态聚点正是补上这一量词差别。

## 10. 正常性边界与仍开放的 Haar 问题

在原 Haar 表示中，
$$
N_j\longrightarrow I/2\quad\text{WOT},\qquad \sup_j\|N_j\|=1.
\tag{10.1}
$$
因一致有界，(10.1) 也对每个正常泛函成立。
具体地，有限秩泛函由 WOT 收敛得到极限，
一般迹类泛函再按迹范数逼近。

如果 $\varphi|_{\mathcal A}$ 有原 Haar 正常延拓 $\omega$，
则 $\omega(I)=1$，所以
$$
\varphi(N_{j_k})=\omega(N_{j_k})\longrightarrow1/2,
$$
与 (1.3) 矛盾。
不只是正正常延拓被排除，任何正常线性延拓都被排除。

在负整数边界中，$\mathsf N_j$ 对每个固定有限头
$\mathscr F_m$ 在 $j\ge m$ 时严格为零。
结合 $\|\mathsf N_j\|\le1$，有
$$
\mathsf N_j\longrightarrow0\quad\text{SOT}.
$$
因此边界正常泛函在 $\mathsf N_{j_k}$ 上也必须趋于0。
(1.3) 同样排除此正常表示。

本文没有把“不是正常态”加强成未经证明的正常/奇异分解结论，
也没有将边界核向量当作原 Haar 向量。

现在必须区分两种命题：

1. 全 Banach 商对偶中的弱零：已由 (9.1) 否定。
2. 仅对可从 Haar 正常泛函下降的湮灭泛函，
   是否有足以推出其在 $I$ 上为零的额外约束：仍开放。

第二条仍是原 Haar 强闭主理想与普遍限制值域问题的相关入口。
本稿中的固定正湮灭态明确位于它之外。

## 11. 依赖与新增部分

- [R174：负整数边界的等距 $*$ 表示](../results/R174-last-column-boundary-state-and-negative-integer-shift.md)，§4。
- [R185：$N$ 慢符号的真实有限块修复](../results/R185-slow-additive-boundary-kernel-and-nonstandard-closed-ideal.md)，§§2–6、8。
- [R188：Cayley 慢符号的逆差与同一修复预算](../results/R188-critical-first-chaos-nonstandard-closed-principal-ideal.md)，§§2–5、7。
- R12 的原 Haar 高位弱极限，仅用于 §10 的正常性判别。

R185/R188 的单个核向量及有限修复公式是已证明输入。
新增内容是：弱首步修复的封闭用途、重复追加固定长度纯核相干块、
全部旧选定位期望的可和保持，以及由这些向量态构造一个固定
$\mathfrak U$ 正状态，实际否定商归一化幂的全对偶弱零。
