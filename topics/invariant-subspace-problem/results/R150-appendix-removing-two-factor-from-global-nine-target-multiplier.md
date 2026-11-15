# R150：从九目标的全局乘子中严格删除二点因子

日期：2026-11-15 UTC。作者：AI（ChatGPT；Astra-ISP-789f / root、literature_audit）。

状态：本篇连接已经完成的原二点有理局部证明、原完整射影确定因子和同一来源次数整理，不运行新的数学计算。结论适用于原十七式的次数至多三来源模块。

## 1. 原来源和删除因子定理

置
$$
L=\operatorname{im}_{\mathbb Q[s]}A\subseteq\mathbb Q[s]^{4367},
\qquad
A:\mathbb Q[s]^{6188}\longrightarrow\mathbb Q[s]^{4367},
$$
并保持全部原来源和输出。九个目标为
$$
t_j=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
$$
[二点完整局部定理](R150-appendix-two-complete-third-connection-smith12-and-all-original-square-local-membership.md)已经证明
$$
t_j\in L_{(s-2)}
\quad(2\le j\le10),
$$
其中下标表示原局部环 $\mathbb Q[s]_{(s-2)}$。该定理保留全部原 $6188$ 来源，完成特征零正谱 $1^7,2,3$，再由完整原投影的同长十二证明整个正常平方目标模局部入像。

因此，对任意 $a(s)\in\mathbb Q[s]$、任意整数 $k\ge0$，都有
$$
\boxed{
(s-2)^k a(s)t_j\in L
\quad\Longleftrightarrow\quad
a(s)t_j\in L.
}
\tag{1.1}
$$

证明只需考虑 $k=1$。由右式推出左式显然。反向令 $b=a(s)t_j$ 并假设 $(s-2)b\in L$。在素点 $(s-2)$，已付的原局部来源给 $b\in L_{(s-2)}$。在任一其他不可约素点 $(f)$，$s-2$ 是单位，所以由假设得到 $b\in L_{(f)}$。有限生成 $\mathbb Q[s]$ 模 $\mathbb Q[s]^{4367}/L$ 中的类 $[b]$ 因而在全部最大理想处为零；局部判准给 $[b]=0$。迭代得到 (1.1)。

这没有对某个既有来源向量逐坐标除以 $s-2$；结论是原固定来源模块中的成员性。局部判准保证另一个多项式来源存在。

## 2. 对原共同候选的准确后果

沿用
$$
h_0=s^3(s-2)F_+^2F_-^2E_8,
\qquad
h_*=\frac{h_0}{s-2}=s^3F_+^2F_-^2E_8.
$$
这里 $F_\pm,E_8$ 仍是原实际多项式，$\deg h_0=24$、$\deg h_*=23$。式 (1.1) 同时给
$$
\boxed{
h_0t_j\in L\ \Longleftrightarrow\ h_*t_j\in L
\quad(2\le j\le10).
}
\tag{2.1}
$$
全部九列同时成立的命题也等价。因此原 $s-2$ 因子不会帮助消去九目标尚未处理的全局商类；删除它不需要预先解决其他有限支撑。

这仍没有证明任一侧的全局成员性。尚未付清的有限异常支撑可能承载其他扭类。

## 3. 真正 gcd 余因子在二点是单位

令 $\Delta_{\mathrm{aff}}$ 为原全部 $4354$ 阶最大子式的特征零 gcd，保持此前实际公共因子
$$
K_{158}
=s^{66}(s-2)^{12}(s+6)^{12}F_+^6F_-^6E_8^4,
\qquad
R=\Delta_{\mathrm{aff}}/K_{158}\in\mathbb Q[s]\setminus\{0\}.
$$
[原无穷远小投影的完整有理谱](R150-appendix-infinity-original-projection-exact-length61-and-full-length-gap-five.md)第 6 节已经证明
$$
\deg\Delta_{\mathrm{aff}}\le320,\qquad
\deg R\le162,\qquad
Rh_0t_j\in L.
\tag{3.1}
$$
这些结论使用完整射影 gcd 次数至多 $381$、真实无穷阶至少 $61$ 及已付的 $K_{158}$，并未把有限域仿射次数当作特征零上界。

本次二点完整长度准确为十二，故
$$
v_{s-2}(\Delta_{\mathrm{aff}})=12
=v_{s-2}(K_{158}).
$$
于是
$$
\boxed{R(2)\ne0.}
\tag{3.2}
$$
这里使用的是完整原确定因子，不只是某个所选子式或投影下界。

将 (1.1) 用于 (3.1)，得到同一个 $R$ 的全局原来源结论
$$
\boxed{
Rh_*t_j\in L\quad(2\le j\le10),\qquad
\deg(Rh_*)\le185.
}
\tag{3.3}
$$

## 4. 九个来源的统一成本仍为 8531

继续使用[已付九来源的全局成本整理](R150-appendix-global-residual-multiplier-nine-sources-cost8531.md)中的同一选定原方阵、原总权 $8770$、无穷阶 $130/125/125$ 及 $K_{158}$。置 $d_*=D/K_{158}$，则
$$
8369\le\deg d_*\le8482.
$$
新的目标 $b_j=Rh_*t_j$ 只有二次 $m$ 输出，其自然权界为
$$
\tau(b_j)\le\deg R+23+2j+20\le225.
$$
式 (3.3) 已经支付多项式来源成员性，所以原伴随式除以 $K_{158}$ 的多项式性及三支余式整理都可直接使用。三个来源成本分支分别为
$$
\begin{aligned}
\text{非基来源}&\le8482-1+45=8526,\\
\text{原来源转移}&\le8770+55-125-158-11=8531,\\
\text{目标伴随支路}&\le8770+225-125-158-10-8369=333.
\end{aligned}
$$
因此存在九个同原 $6188$ 坐标的多项式来源 $x^{(j)}$，满足
$$
\boxed{
Ax^{(j)}=Rh_*t_j,\qquad
\operatorname{cost}(x^{(j)})\le8531
\quad(2\le j\le10).
}
\tag{4.1}
$$
共同的 $R$ 没有被展开计算；本篇不提供系数高度或固定素数分母。不因目标支路下降一就改变仍由原来源转移决定的总成本。

## 5. 结论边界

式 (1.1) 是原九目标模在二点因子上的饱和性，式 (3.2) 是真正完整 gcd 余因子的二点单位性。式 (3.3) 和 (4.1) 给次数至多 $185$ 的共同参数乘子及统一成本 $8531$。

$R$ 的其余因子是否必要仍需逐个原局部来源或完整支撑定理。原完整临界点的集合分类、原泛型 $\mathbb Q(s)$ 像，以及线性块 $D_{\mathrm{lin}}$ 的单位性，都不能未经来源次数证明就替代这个有限来源模块的局部成员性。本篇不声称 $R$ 为常数，也不声称原 $h_*$ 或 $h_0$ 已经全局入像。
