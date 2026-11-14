# R253 附录：全部 first 共同域仍不包含于慢符号值域

日期：2026-11-13（UTC+8）。作者：normal_states / Astra-ISP-1cf。状态：已证明的实际分母障碍；不排除 R244 中针对某个湮灭见证选择的配对正则器。

本稿证明：对慢符号 $S_N,S_Y$，即使向量同时属于全部 $\ell^2$ first 乘子的定义域，也不能保证它属于 $\operatorname{Ran}S$。因此，任意一个有界 first 预解式都不能写成 $SR$，其中 $R$ 为有界算子；这里甚至不要求 $R$ 交换。证明保留真实 carry，并分别核查共同域的 Banach 完备性与交换域。

## 1. 设定和 R125 的实际域接口

仍在原 Haar 空间
$$
H=\bigotimes_{j\ge0}(\mathbb C^2,\Omega_+)
$$
上工作。记
$$
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad
0<\eta_j\le e^{-770\,16^j},
$$
$$
Y_j=N_j(I+N_j)^{-1},\qquad
V_j=I-2Y_j,\qquad
V_j^0=I-2E_j.
$$
这里 $E_j=e_{10}^{(j)}$ 是物理单个位创建算子。
令
$$
a_j=(j+1)^{-2},\qquad a_\Sigma=\sum_ja_j,\qquad
S_N=\sum_ja_jN_j,\qquad S_Y=\sum_ja_jY_j.
\tag{1.1}
$$
这两个 $S$ 都属于 $\mathcal A$，并已由 R122/R124 证明单射。

对 $b=(b_j)\in\ell^2$，令 $X_b$ 为 R125 的实际闭 first 乘子。
本稿把额外标量常项留给预解参数 $\lambda$。
R125 已证：有限 Walsh 柱同时为 $X_b$ 及其通常伴随的图核心；
在该核心上，
$$
X_bf=\sum_jb_jV_jf,\qquad
X_b=X_b^0+K_b,\qquad
K_b=\sum_jb_j(V_j-V_j^0),
\tag{1.2}
$$
其中
$$
\|V_j-V_j^0\|\le8\eta_j,\qquad
\|K_b\|\le8\|\eta\|_2\|b\|_2.
\tag{1.3}
$$
$X_b^0$ 只在本稿的有限柱计算中使用；其闭实现的其他性质不需要另行假设。

### 1.1 $S$ 真正保持 first 域

对每个 $b$，实际 $X_b$ 按域与 $A$ 交换。
因而每个多项式 $p(A)$ 保持 $\operatorname{Dom}X_b$，
且 $X_bp(A)f=p(A)X_bf$。
若 $p_n(A)\to S$ 于算子范数，且 $f\in\operatorname{Dom}X_b$，则
$$
p_n(A)f\to Sf,\qquad
X_bp_n(A)f=p_n(A)X_bf\to SX_bf.
$$
由 $X_b$ 闭，
$$
\boxed{
S\operatorname{Dom}X_b\subseteq\operatorname{Dom}X_b,\qquad
X_bSf=SX_bf.
}
\tag{1.4}
$$
后文所有 $X_bSu_m$ 都由这个真实闭域步骤定义，不把形式交换当成域交换。

## 2. 全 1 物理头上的准确 carry 衰减

对 $m\ge1$，定义等距嵌入
$$
W_m:H_m\to H,\qquad
W_mv=e_1^{\otimes m}\otimes v,\qquad
u_m=W_m\Omega_m.
\tag{2.1}
$$
$u_m$ 是单位有限柱向量；在 Walsh 坐标中
$$
u_m=2^{-m/2}\prod_{j<m}(1-\chi_j).
$$
令
$$
\varepsilon_m=e^{-770\,16^{m-1}},\qquad
A_m=\sum_{j\ge m}a_j\le\frac1m.
\tag{2.2}
$$

若 $j<m$，$E_j$ 杀掉输入的物理位 $e_1$。
逐级使用实际递归，准确得到
$$
N_jW_mv=
\left(\prod_{\ell=j}^{m-1}\eta_\ell\right)
e_1^{\otimes j}\otimes e_0^{\otimes(m-j)}
\otimes\widehat N_mv.
\tag{2.3}
$$
因此
$$
\|N_jW_m\|\le\varepsilon_m\qquad(j<m).
\tag{2.4}
$$
又
$$
(I+N_j)^{-1}=(I-N_j)(I-N_j^2)^{-1},
\qquad
\|(I+N_j)^{-1}\|
\le\frac2{1-\eta_j}<3.
$$
利用 $Y_j=(I+N_j)^{-1}N_j$，得
$$
\|Y_jW_m\|\le3\varepsilon_m.
\tag{2.5}
$$
对 $j\ge m$，$N_j,Y_j$ 只作用于尾，且范数分别至多 $1,3$。
所以对两个慢符号都可统一取
$$
\boxed{
\|SW_m\|\le3(A_m+a_\Sigma\varepsilon_m),\qquad
\|S\|\le3a_\Sigma.
}
\tag{2.6}
$$

还需要 carry 在 first 图范数中的真实控制。
对于 $j<m$，$V_j^0W_m=W_m$，故
$$
(V_j-V_j^0)W_m=-2Y_jW_m,\qquad
\|(V_j-V_j^0)W_m\|\le6\varepsilon_m.
$$
对 $j\ge m$ 使用 (1.3)。
由
$$
\left(\sum_{j\ge m}\eta_j^2\right)^{1/2}
\le2e^{-770\,16^m}\le2\varepsilon_m
$$
及 Cauchy–Schwarz，得到
$$
\boxed{
\|K_bW_m\|
\le(6\sqrt m+16)\varepsilon_m\|b\|_2.
}
\tag{2.7}
$$
因此这里控制了整个嵌入尾空间上的实际误差，而不只是单个真空矩。

## 3. $Su_m$ 在全部 first 图范数中统一趋零

置
$$
B_m(b)=\sum_{j<m}b_j,\qquad
h_{m,b}=\sum_{j\ge m}b_j\chi_j\in H_m.
$$
纯局部式在有限柱 $u_m$ 上给出
$$
X_b^0u_m=W_m\bigl(B_m(b)\Omega_m+h_{m,b}\bigr),
\quad
|B_m(b)|\le\sqrt m\|b\|_2,\quad
\|h_{m,b}\|=\|b_{\ge m}\|_2.
\tag{3.1}
$$
由 (1.4)、(2.6)、(2.7)，
$$
\begin{aligned}
\|X_bSu_m\|
&=\|SX_bu_m\|\\
&\le
3(A_m+a_\Sigma\varepsilon_m)
\bigl(|B_m(b)|+\|b_{\ge m}\|_2\bigr)
+3a_\Sigma(6\sqrt m+16)\varepsilon_m\|b\|_2.
\end{aligned}
\tag{3.2}
$$
特别，
$$
\boxed{
\|Su_m\|\to0,\qquad
\sup_{\|b\|_2\le1}\|X_bSu_m\|
\le3(A_m+a_\Sigma\varepsilon_m)(\sqrt m+1)
+3a_\Sigma(6\sqrt m+16)\varepsilon_m
\longrightarrow0.
}
\tag{3.3}
$$
右侧为 $O(m^{-1/2})$。
对每个固定 $b$，另有 $B_m(b)=o(\sqrt m)$；
把前面固定有限段与 $\ell^2$ 尾分开即可证明。
所以固定 $b,\lambda$ 时甚至有
$$
\|(\lambda+X_b)Su_m\|=o(m^{-1/2}).
\tag{3.4}
$$
只需要 (3.3) 就足以证明下述结论。

## 4. 全部 $\ell^2$ first 共同域是实际 Banach 空间

定义
$$
\mathcal E=
\bigcap_{b\in\ell^2}\operatorname{Dom}X_b.
\tag{4.1}
$$
先证明对每个 $f\in\mathcal E$，线性映射
$$
T_f:\ell^2\to H,\qquad T_fb=X_bf
$$
自动有界。这一步不能只从“每个 $X_b$ 闭”直接省略。

若有限柱 $v$ 只使用前 $n$ 位，纯局部高位的
$(V_j^0)^*v=-\chi_jv$、$j\ge n$，互相正交；
低位为有限和，且 $\|V_j^0\|\le3$。
结合 (1.3)，有
$$
\|X_b^*v\|
\le(3\sqrt n+1+8\|\eta\|_2)\|b\|_2\|v\|.
\tag{4.2}
$$
因此 $b\mapsto X_b^*v$ 为连续的共轭线性映射。
通过在所有有限柱 $v$ 上配对，$T_f$ 的线性性直接成立。
若 $b_k\to b$ 于 $\ell^2$，且 $X_{b_k}f\to g$ 于 $H$，
则由 (4.2)，
$$
\langle g,v\rangle
=\lim_k\langle f,X_{b_k}^*v\rangle
=\langle f,X_b^*v\rangle
=\langle X_bf,v\rangle.
$$
有限柱稠密，故 $g=X_bf$。
所以 $T_f$ 是全域闭线性映射，闭图定理给 $T_f\in B(\ell^2,H)$。

在 $\mathcal E$ 上取范数
$$
\|f\|_{\mathcal E}=\|f\|+\|T_f\|
=\|f\|+\sup_{\|b\|_2\le1}\|X_bf\|.
\tag{4.3}
$$
这是完备范数。事实上，若 $f_n$ 在此范数中 Cauchy，
则 $f_n\to f$ 于 $H$，且 $T_{f_n}\to T$ 于 $B(\ell^2,H)$。
对每个固定 $b$，由闭的 $X_b$，
$$
f\in\operatorname{Dom}X_b,\qquad X_bf=Tb.
$$
故 $f\in\mathcal E$ 且 $T_f=T$，证明完备性。

有限柱属于 $\mathcal E$，可用与 (4.2) 相同的纯局部正向计算验证。
由 (1.4)，$S\mathcal E\subseteq\mathcal E$，
且 $T_{Sf}=ST_f$。
特别，(3.3) 精确给
$$
\boxed{Su_m\longrightarrow0\quad\text{于 }\mathcal E.}
\tag{4.4}
$$

## 5. 全 first 共同域仍不包含于 $\operatorname{Ran}S$

**定理。** 对 $S=S_N$ 或 $S_Y$，
$$
\boxed{
\mathcal E\not\subseteq\operatorname{Ran}S.
}
\tag{5.1}
$$

反设 $\mathcal E\subseteq\operatorname{Ran}S$。
$S$ 单射，故
$$
S^{-1}:\mathcal E\longrightarrow H
$$
为全域线性映射。
它的图闭：若 $v_n\to v$ 于 $\mathcal E$，且 $S^{-1}v_n\to u$ 于 $H$，
则 $v_n\to v$ 于 $H$，从 $S(S^{-1}v_n)=v_n$ 得 $Su=v$；
由单射性，$u=S^{-1}v$。
两个空间都是 Banach 空间，所以闭图定理迫这个逆映射有界。
但 (4.4) 与 $\|u_m\|=1$ 给
$$
S^{-1}(Su_m)=u_m,\qquad
Su_m\to0\text{ 于 }\mathcal E,
$$
矛盾。定理得证。

因此存在一个向量，属于所有 $\ell^2$ first 定义域，却不在慢符号值域中。
这是存在性结论；本稿没有给出该向量的闭式表达。

任意预先给定可数族 $b^{(r)}$ 的共同域也不包含于 $\operatorname{Ran}S$，
因为它包含 $\mathcal E$。
该可数版本还可独立核验：取由
$\|f\|+\sum_{r\le n}\|X_{b^{(r)}}f\|$ 定义的 Fréchet 拓扑，
闭性保证其完备，(3.3) 给 $Su_m\to0$，
再对全域逆用 Fréchet 到 Banach 的闭图定理得到同一矛盾。
不可数加强来自第 4 节单独证明的 Banach 图范数，
不是把可数闭图论证直接外推。

## 6. 有界 first 预解式不能作为这个理想的有界分母

设某个 $b\in\ell^2$ 及 $\lambda\in\mathbb C$ 满足
$$
L=(\lambda I+X_b)^{-1}\in B(H).
$$
则
$$
\boxed{
L\notin S B(H),\qquad
\operatorname{Ran}L\not\subseteq\operatorname{Ran}S.
}
\tag{6.1}
$$
一种直接证明不需要交换任何未知因子。
若 $SR=L$，$R\in B(H)$，置
$$
v_m=(\lambda+X_b)Su_m.
$$
由真实域 (1.4)，该向量有定义；由 (3.3)，$v_m\to0$。
而
$$
SRv_m=Lv_m=Su_m.
$$
取消单射的 $S$，得到 $Rv_m=u_m$，与 $R$ 有界、$\|u_m\|=1$ 矛盾。
若只假设 $\operatorname{Ran}L\subseteq\operatorname{Ran}S$，
则全域闭算子 $S^{-1}L$ 由闭图定理有界，又回到上述矛盾。
整个论证均不要求 $R\in\{A\}'$。

因此，不能仅从正 first 逆的近真空作用和范数控制，
就把它收入慢符号理想作为 R253 的统一真空测试。
这是一条针对实际 $S^{-1}$ 的分母障碍。

## 7. 与尚未解决问题的界限

本稿没有证明 $\mathcal E$ 中不存在可用的个别向量，
也没有排除更高混合词图域、某个 first 预解式乘积的像，
或依赖未知正常见证的其他交换正则器。
尤其，R244 只要求指定有限输入的配对域，并不要求其正则器属于 $S B(H)$；
不能把 (6.1) 当作 R244 不可能的结论。

R253 的完整理想测试量
$q_m=\|\omega_m|_{\overline{Q_m\mathcal B_m}}\|$
是否一致离开零，仍需其他实际估计。
本稿只排除了通过上述 first 域为 $S^{-1}$ 选择一个全域有界分母的自然尝试，
不以失败记录代替原正常湮灭者问题或普通 ISP 的完成。
