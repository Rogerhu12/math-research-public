# R365：清除整个原导子角连接的真实次数三十七 carrier

日期：2026-11-13。**状态：以下整个原 canonical 来源上的次数三十七整算子、全部 floor 边界、总 Euler \(\mathcal E+40\) 的完整物理转置及十行运输成本均已证明。固定 \(P_{134}\) 的对数导数由真实归一化乘子支付，没有将其零点或原 \(U_0\) 连接删除。该算子作用于整个来源；未给各次数分量单独附加中央零。**

## 1. 原整个来源和公共角因子

采用 R335、R351、R352 的记号
\[
h_7=16t^2+4t+7,\quad a=t(t-1)h_7,\quad
\chi=(t-1)(1+8t)h_7,\qquad
\rho=\Theta^{17}(1+8t).
\]
相对径向变量记为 \(\mathscr R\)。
原来源次数 \(n\) 的完整整格为
\[
\mathcal V_n=\mathscr R^n q_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=\frac{(t h_7)^{\alpha_n}(t-1)^{\beta_n}}{(1+8t)^{\gamma_n}},
\]
\[
\alpha_n=\lfloor(n+1)/4\rfloor,\quad
\beta_n=\lfloor(n+1)/3\rfloor,\quad
\gamma_n=\lfloor n/2\rfloor,\quad
\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4 .
\tag{1}
\]
固定单位倍不影响下文；原共同来源准确可写为
\[
\boxed{
G_0=\mathscr R^{40}h_0(t),\qquad
h_0(t)=
\frac{P_{134}(t)t^{13}(t-1)^{15}h_7^{13}}{(1+8t)^{17}}.
}
\tag{2}
\]
\(P_{134}\) 是 R335 的实际 primitive 多项式，
\[
P_{134}(0)=-3^4\cdot3159421.
\]
因此真正的原列为 \(G_0\Phi\)，原 charge 是相对次数加40。
本篇保留全部 \(P_{134}\)，不先删去它与测试多项式的公共分量。

## 2. 一个真正的次数三十五乘子及全 floor 检查

R325/R335 的次数 \(m\) 归一化基本分式为
\[
\mathscr R^m u_m(t),\qquad
u_m=
\frac{(t h_7)^{\lceil m/4\rceil}(t-1)^{\lceil m/3\rceil}}
{(1+8t)^{\lfloor m/2\rfloor}},
\]
允许的多项式次数为
\[
d_m=3\lfloor3m/4\rfloor+2\lfloor m/2\rfloor+\lfloor2m/3\rfloor.
\]
特别
\[
d_{35}=135,\qquad d_{34}=131.
\]
定义真实归一化元素
\[
\boxed{
V=\mathscr R^{35}
 \frac{t^9(t-1)^{12}h_7^9}{(1+8t)^{17}}P_{134}(t)
\in\mathcal N_{35}.
}
\tag{3}
\]
本次构造用的是完整的 \(P_{134}\)，其次数134已在 \(d_{35}\) 内支付。

不只核无穷次数：对任意原次数 \(n\)，令
\[
\Delta_\alpha=\alpha_{n+35}-\alpha_n\in\{8,9\},\quad
\Delta_\beta=\beta_{n+35}-\beta_n\in\{11,12\},\quad
\Delta_\gamma=\gamma_{n+35}-\gamma_n\in\{17,18\}.
\]
准确有
\[
\frac{u_{35}q_n}{q_{n+35}}
=(t h_7)^{9-\Delta_\alpha}
(t-1)^{12-\Delta_\beta}
(1+8t)^{\Delta_\gamma-17}\in\mathcal O[t].
\tag{4}
\]
全部显示指数非负，所有固定零极都保留。
又
\[
\deg(u_{35}P_{134})=156
<\lfloor9(n+35)/2\rfloor-\lfloor9n/2\rfloor,
\]
右边是157或158。因此对所有 \(n\)
\[
V\mathcal V_n\subset\mathcal V_{n+35}.
\tag{5}
\]
同一证明也适用于把 \(P_{134}\) 换成 \(tP_{134}'\)，
因为其次数仍不超过134。
这给后面的完整对数导数项所需的真实整来源。

## 3. 清全部角连接的整算子

沿 R352 取
\[
W_2=\mathscr R^2a\chi,\qquad
\mathcal Q_2=W_2t\partial_t,\qquad
\mathcal E=\mathscr R\partial_{\mathscr R}.
\]
R352 已对全部 floor 类证明
\[
W_2\mathcal V_n,\quad \mathcal Q_2\mathcal V_n
\subset\mathcal V_{n+2}.
\]
置
\[
\boxed{\mathscr M=V W_2\in\mathcal N_{37}.}
\tag{6}
\]
公共角连接为
\[
\eta_0=t\partial_t\log h_0
=13+\frac{15t}{t-1}
+\frac{13t h_7'}{h_7}
-\frac{136t}{1+8t}
+\frac{tP_{134}'}{P_{134}} .
\tag{7}
\]

**定理1。** 以下两个算子都是真正原来源的整映射：
\[
\boxed{
\mathcal T=\mathscr M(t\partial_t+\eta_0):
\mathcal V_n\longrightarrow\mathcal V_{n+37},
}
\tag{8}
\]
\[
\boxed{
\mathcal D_{\rm tot}
=\mathcal T+\mathscr A(\mathcal E+40),
\qquad
\mathscr A=\mathscr M c(t),\quad
c(t)=\frac{8t}{1+8t}-\frac{17}{3}.
}
\tag{9}
\]
\(t\partial_t\) 保持 \(\mathscr R\) 不动。

**证明。** \(\mathscr M t\partial_t=V\mathcal Q_2\) 的闭合由 (5) 和 R352 给出。
先从 (7) 去掉 \(P_{134}\) 项，其余各项乘 \(W_2\) 都属于 \(\mathcal N_2\)：
相对基本分式
\(\mathscr R^2t(t-1)h_7/(1+8t)\)，对应商均为次数至多五的整多项式。
它们分别使用
\[
(t-1)(1+8t)^2h_7,\quad
t(1+8t)^2h_7,\quad
t(t-1)(1+8t)^2h_7',\quad
t(t-1)(1+8t)h_7 .
\]
常数系数13、15、13、\(-136\) 均保留。

最后一项准确为
\[
\mathscr M\,\frac{tP_{134}'}{P_{134}}
=W_2\,\mathscr R^{35}u_{35}\,tP_{134}'.
\]
其次数三十五因子已由 (4)、(5) 的同一全 floor 证明支付。
所以 (8) 整闭合，不在 \(P_{134}\) 根处丢项。

R351 已核 \(W_2c\in\mathcal N_2\)，故
\(\mathscr A=V(W_2c)\in\mathcal N_{37}\)。
\(\mathcal E+40\) 在原次数 \(n\) 上准确乘 \(n+40\)，
因而 (9) 也整闭合。\(\square\)

此算子是在实际 \(G_0\Phi\) 上取完整角导数：
\[
\mathscr M\,t\partial_t(G_0\Phi)=G_0\mathcal T\Phi .
\]
固定 \(P_{134}\) 没有被当作单位；它的导数由原整数列实际实现。

## 4. 总 charge 的完整物理转置

取
\[
p=6s-1,\quad s>23,\quad
1\le\ell<s-23,\quad L=2s+\ell,\quad T=L+13.
\tag{10}
\]
这样 \(T+10<3s\)，新增十行仍完全处于同一个三块目标，
不需要未经支付的第四块。

令 \(F_-\) 表示原完整来源 \(G_0\Phi\) 到 \(\Gamma_T\) 的实际评价，
\(F_+\) 表示来源次数上限加37、目标长度加10的实际评价。
也就是说
\[
F_\pm=U_0M_\pm
\]
用同一个原单位的相应完整截断；
\(M_\pm\) 仍是 R351 的 \(m_{13}J\) 规范。
定义
\[
B_{37}=\mathscr M_{\rm phys}\nu,\qquad
Z_{37}=\mathscr M_{\rm phys}\frac{x\zeta}{y},
\quad
\nu=\frac{(1-t)^{-1/2}}{h(t)},\quad
\Lambda=\mathsf E_w\log\rho.
\]
R351 的完整物理式为
\[
\nu\mathsf E_w=-xD_z/(6y),\qquad
\nu\Lambda=c(t)-17x\zeta/(3y).
\]

**定理2。** 在整个原来源上准确有
\[
\boxed{
F_+\mathcal T
=B_{37}\{\mathsf E_wF_-
-\Lambda F_-(\mathcal E+40)\},
}
\tag{11}
\]
以及
\[
\boxed{
F_+\mathcal D_{\rm tot}
=B_{37}\mathsf E_wF_-
+\frac{17}{3}Z_{37}F_-(\mathcal E+40).
}
\tag{12}
\]

**证明。** 对实际源 \(G_0\Phi\) 使用链式法则。
其径向 Euler 准确为 \(G_0(\mathcal E+40)\Phi\)，
角导数准确由 (8) 实现；
全部高 Gaussian 轴仍在 \(\Lambda\) 中。
这给 (11)。再用 (9) 和 \(\nu\Lambda\) 的准确值，
有理部分由真正来源 \(\mathscr A(\mathcal E+40)\Phi\) 支付，得到 (12)。\(\square\)

若把 (12) 写回原 \(m_{13}\) 目标规范，准确形式是
\[
\boxed{
M_+\mathcal D_{\rm tot}
=B_{37}\left(\mathsf E_w+\frac{\mathsf E_wU_0}{U_0}\right)M_-
+\frac{17}{3}Z_{37}M_-(\mathcal E+40).
}
\tag{13}
\]
这里的公共连接没有删除。
事实上
\[
\frac{\mathsf E_wU_0}{U_0}
=40\Lambda+\eta_0/\nu-13.
\]
代回 (13) 就恢复 R351 的十三行与角连接形式。
\(U_0\) 只在原形式目标中是已付单位；
到非原点测试极的 \(Z^{-78}\) 行移及其所有角零仍须保留。

对每个 \(r\ge1\)，若 \(P_r\in K_r(F_-)\)，则 (12) 立即给
\[
\boxed{
Z_{37}F_-((\mathcal E+40)P_r)
\in\operatorname{im}(F_+\bmod p^r).
}
\tag{14}
\]
这仍是原像成员性；没有假定 \(\mathcal E+40\) 保持核。

## 5. 精确物理首阶与二十条边界

由 \(t=-bw+\cdots\)、\(\rho(0)=\nu(0)=1\)，
\[
V_{\rm phys}
=3^4\,7^9b^9\cdot3159421\,w^9+\cdots.
\]
又 \(W_{2,\rm phys}=-49b\,w+\cdots\)，所以
\[
\boxed{
B_{37}=
-3^4\,7^{11}b^{10}\cdot3159421\,w^{10}
\times(\text{原完整整单位}).
}
\tag{15}
\]
因此只需再排除 \(p\mid3159421\)；
其他固定素数已在原好位中排除。
同一条件下 \(Z_{37}\) 也是 \(w^{10}\) 乘整单位。

这不是原点单位乘子。
在完整基 \(e_r=w^r/p^{\lfloor r/s\rfloor}\) 上，
乘 \(w^{10}\) 的系数为
\[
p^{\lfloor(r+10)/s\rfloor-\lfloor r/s\rfloor}.
\]
在 (10) 的两个完整目标中，准确只有
\[
s-10\le r<s,\qquad 2s-10\le r<2s
\tag{16}
\]
这二十行带一个 \(p\)，其余都是单位。
所以对任意原整源矩阵 \(H\) 和任意精度 \(h\)
\[
\boxed{
0\le
\operatorname{length}\ker(w^{10}H\bmod p^h)
-\operatorname{length}\ker(H\bmod p^h)
\le20.
}
\tag{17}
\]
原来 \(m_{13}\) 的二十六行成本仍保留；
本篇只新增这二十条边界。
固定 charge37 的来源代价也没有因 (17) 而免除。

## 6. 与 R363 原二阶有理连接模型的完整对接

R363 给出的原有限代表
\[
R_{\kappa,p}^{(2)}\equiv(x/y)\zeta_\kappa\pmod{p^2\Gamma}
\]
保原点值、全部真实测试点及其单位一阶 jet。
由于 (10) 的全部目标仍在 R363 已付窗口内，
\[
\boxed{
Z_{37}\equiv
\mathscr M_{\rm phys}R_{\kappa,p}^{(2)}
-\frac{(p+1)a_\kappa}{34}B_{37}\epsilon
\pmod{p^2}.
}
\tag{18}
\]
因此 (12) 给同一个原完整矩阵上的显式模 \(p^2\) 恒等式
\[
\boxed{
F_+\mathcal D_{\rm tot}\equiv
B_{37}\mathsf E_wF_-
+\frac{17}{3}
\left\{\mathscr M_{\rm phys}R_{\kappa,p}^{(2)}
-\frac{(p+1)a_\kappa}{34}B_{37}\epsilon\right\}
F_-(\mathcal E+40)
\pmod{p^2}.
}
\tag{19}
\]
所有 Gaussian、first-lift 和固定 carrier 项均在这一式中。
对原 \(P\in K_2(F_-)\)，新增的 \(40P\) 在
\(\epsilon F_-((\mathcal E+40)P)/p\) 中贡献为零模 \(p\)；
原两条接触尾仍由 R338 的同一个 \(P\) 决定。

在单一来源次数 \(n\) 上，原完整 theta 因子是
\(\Theta^{17(n+40)}\)，其自然局部连接指数为
\[
m_n=34(n+40)>0.
\]
这个正号与 R361 的局部扭残数规范相容。
但 \(n\) 是来源次数，不能与 forcing 的 \(q_j\) 指标混同，
也不能将一个混合次数的原核向量拆成逐次数的核。
(19) 提供的是整个来源上的同一个实际算子，
保留这一必要的耦合。

本篇全体 floor 和来源证明是参数恒等式，
没有以数值抽查替代；没有增加原完整中央零。
文件通过已授权的 GitHub API 保存；核心同步记录由根代理维护。
