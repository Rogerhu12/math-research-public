# R698 — 保旧 17² 类的 A 三十四层返回与未删角型的 CM 算术词

日期：2026-11-15。**状态：已证明。**

R695 的原 A 两层与 Z 一层有相同的三态来源矩阵，但完整 CM 来源需要
一个更大的共同格。本篇保留当前已经固定的 $17^2$ 类，付清这个差别。
原 A 的**三十四层**在整个共同格上准确回到二挠算子；
经确切单位旋转后的第一 CM13/19 与它逐项交换。
由此得到同一个未作角平均的固定 CM 来源上的 A/Y/Z 算术词，
不再把每条 CM 分支的词域各自共轭。

这里没有声称第一角平均 $\Pi_0$ 与 A 深条件交换。
相反，给出它在完整格上不交换的明确证据。
算术识别只在整个词返回以后，利用原 principal Y 测试完成。
原全部门、多项式和词域补集均保留。

## 1. 旧射线实际已固定到 17²

原 R410 给 $\pi_0\equiv1+2\omega\bmod17$。
但 R487 的 CRT 程序实际采用
$$
M_0=712345233600=255\cdot2793510720,\qquad
(a_0,b_0)=(1428552127,2161889730)
\tag{1}
$$
作为旧类；它含 $17^2$，不只含 17。
R487 的高 $13^{34},19^{10}$ 条件保留 (1)；
R500 程序又明确从该 new_ray 开始，只增加 29、137。
R503 使用该同一射线，R522 不改变它。
因此当前类在 $17^2=289$ 准确为
$$
\boxed{\pi_0\equiv273+87\omega,\qquad
       \operatorname{Tr}(\pi_0)\equiv170\not\equiv0\pmod{289}.}
\tag{2}
$$
不能把它换成方便的 $\delta$ 高提升。

使用 $\omega^2+\omega+1=0$ 和 $N\pi_0$ 为单位，
从 (2) 直接计算得
$$
\boxed{
g_\pi=\pi_0/\bar\pi_0\equiv152+17\omega,\qquad
g_\pi^2\equiv1-17\delta\pmod{289},\quad\delta=1+2\omega .
}
\tag{3}
$$
后者在模 289 的单位群中阶恰为 17：
$(1-17\delta)^j=1-17j\delta\bmod289$。
本篇不增加射线条件，也不修改原 M3 或后续固定有限坏集。

## 2. 同一个 Y/A 全张量格

保持 R695 的实际
$$
Q=c+2d,\quad L=2c-d,\quad Y=A+Q,\quad J=5A-29Q.
\tag{4}
$$
$N(A,Q,L)=(29,5,5)$，
$$
\operatorname{Gram}(Y,J,L)=\operatorname{diag}(34,4930,5).
$$
J 是本篇新增的正交物理伙伴，不是 Katz 函数或旧中央导数。

原三个状态 $e_0,e_1,e_2$ 包括原 C 平均和所有 W quarter flats。
它们在同一个
$$
\mathcal S_{136,\,2Y}\otimes
\mathcal S_{19720,\,2J}\otimes
\mathcal S_{80,\,4L}\otimes\mathcal T
\tag{5}
$$
中，$\mathcal T$ 保另外三个原 A 伙伴。
证明只需检查 W 平移的参数。
在 (4) 中
$$
W=b_YY-\frac{3(1+\omega)}{85}J+b_LL,\qquad
b_Y=\frac{20+3\omega}{17},\quad b_L=\frac{2+12\omega}{5}.
$$
在 $2Y,2J,4L$ 上，次数乘参数分别为
$4(20+3\omega)t,-348(1+\omega)t,4(2+12\omega)t$；
对 $t\in E[4]$ 均为原格点。
全部交叉 Gaussian 由上述 Gram 为零支付，原 even 特征也不变。
这保完整联合，不只是将伙伴置零的一变量归属。

生成变量的换元为
$$
a=2z+10t,\quad q=2z-58t.
$$
取原 A、Q 的共同 $[68]$ 拉回后，
$$
\boxed{z=29a'+5q',\qquad t=a'-q'.}
\tag{6}
$$
故 (5) 完整嵌入
$$
\mathcal S_{N_A,\,68A}\otimes
\mathcal S_{N_Q,\,68Q}\otimes
\mathcal S_{80,\,4L}\otimes\mathcal T,
$$
$$
\boxed{N_A=29\cdot68^2=134096,\qquad
       N_Q=5\cdot68^2=23120.}
\tag{7}
$$
直接核得
$$
136\cdot29^2+19720=N_A,\quad
136\cdot5^2+19720=N_Q,\quad136\cdot29\cdot5-19720=0.
$$
因此第一 $2Y$ 的完整 CM 算子仍在这个**固定**共同格中作用。
这一步没有引入依赖 CM 次数的可变覆盖。

## 3. 整个 N_A 空间的准确三十四次核心

令 $K_{N_A,p}$ 是外部 $\lambda=-\bar\pi_0^{-1}$ 已分离后的
原 ordinary theta 核。
除 (3) 外，旧 ray 给
$$
g_\pi^2\equiv25+16\omega\pmod{32},\qquad
g_\pi\equiv1\pmod{29}.
$$
又 $(25+16\omega)^2\equiv17\bmod32$，故它的第十七次仍为自己。
对 $2N_A=32\cdot29\cdot17^2$ 作 CRT，得到
$$
\boxed{
g_\pi^{34}\equiv1+\frac{3N_A}{2}+N_A\omega\pmod{2N_A}.
}
\tag{8}
$$

在整个 $\mathcal S_n$、$16\mid n$ 上，令
$$
B_{2,n}=\frac12\sum_{t\in E[2]}\mathsf T_t^{(n)}-I.
$$
用原 Schrödinger 基、$Xe_j=\zeta_n^je_j,\ Ze_j=e_{j+1}$，
全部中心明确给
$$
\boxed{
B_{2,n}e_j=(-1)^j e_{(1+n/2)j+n/2},\qquad
B_{2,n}^2=I,
}
\tag{9}
$$
$$
B_{2,n}XB_{2,n}^{-1}=-X^{1+n/2},\qquad
B_{2,n}ZB_{2,n}^{-1}=-Z^{1+n/2}.
$$
这实现 (8) 的完整 ratio。
也可用 $1+n/2+n\omega$；乘实中心 $1+n$ 不改这些 canonical lifts，
因为其周期差与原参数同向，交叉指数为零，且 n 偶。

所以 $K_{N_A,p}^{34}$ 与 $B_{2,N_A}$ 只可能相差一个标量。
绝对定标使用原非零 odd29 来源
$$
F_{29}(z)=\sigma(2z)\sigma(5z),\qquad F_{29}(z)=10z^2+\cdots.
$$
R488 的 whole odd29 核是 $\chi_{29,p}I$、$\chi_{29,p}^2=1$。
普通单位 $[68]$ 拉回与真实 restriction/pushforward 交换，
因此 $K_{N_A,p}^{34}$ 在 $F_{29}(68z)$ 上为一。
所有二挠 lift 在这个拉回上也为一：$68t$ 是偶格周期，
原 odd 半特征与 canonical 交叉项均为一。
于是 $B_{2,N_A}$ 同样在此非零锚上为一。严格得到
$$
\boxed{
K_{N_A,p}^{34}=B_{2,N_A},\qquad K_{N_A,p}^{68}=I .
}
\tag{10}
$$

原 $A^2$ 不能在此 whole 空间直接替代 (10)。
它在 $17^2$ Heisenberg 部分的 ratio 是 (3) 的非平凡元，
而 $B_{2,N_A}$ 在该奇部分的 ratio 为一；
二者不是相差标量的完整交织。
34 是消去该奇部分、同时保二挠奇次返回的首个正偶指数。
这不否认 R488 在原三个特定状态上已经成立的 A 两层 R；
区别在于现在要容纳全部第一 CM 来源。

## 4. 准确单位修正后的 CM 与共同 A 核

由 (6) 的完整 Gram，A 二挠 lift 在 (5) 中准确为
$$
\mathsf T_{t,A}^{(N_A)}
=\mathsf T_{29t,\,2Y}^{136}\otimes
 \mathsf T_{t,\,2J}^{19720}\otimes I .
$$
$t\in E[2]$ 时，$29t-t=28t$ 是同向格周期，完整相位为一。
所以 (10) 在 (5) 上变成
$$
\boxed{
\mathcal B_A=\frac12\sum_{t\in E[2]}
 \mathsf T_{t,\,2Y}^{136}\otimes
 \mathsf T_{t,\,2J}^{19720}-I.
}
\tag{11}
$$
它是两个输出的耦合算子，不能删掉第二因子。

第一 $2Y$ 的原两个 CM ratio 已精确定标：
$$
g_{13}=43+147\omega,\qquad g_{19}=87+144\omega\pmod{272}.
$$
令 $\mathsf R_\zeta F(z,\mathbf z)=F(\zeta z,\mathbf z)$，定义
$$
\boxed{
\widetilde N_{13}=\mathsf R_{\omega^2,Y}N_{13,Y},\qquad
\widetilde N_{19}=\mathsf R_{-1,Y}N_{19,Y}.
}
\tag{12}
$$
$\mathsf R_\zeta$ 对平移参数的 ratio 是 $\zeta^{-1}$。
因此它们的完整 ratio 为
$$
\widetilde g_{13}=125+168\omega,\qquad
\widetilde g_{19}=185+128\omega\pmod{272},
\qquad \widetilde g_a\equiv1\pmod4.
\tag{13}
$$
两算子逐个固定第一轴的四个二挠 canonical lift。
参数只差格周期，指数含 $136/2=68$；其符号恰为一。
它们固定第二 J 轴，故完整交换 (11)：
$$
\boxed{
[\widetilde N_{13},\mathcal B_A]
=[\widetilde N_{19},\mathcal B_A]=0.
}
\tag{14}
$$
这是在固定 (5) 的整个联合上的等式，没有留下未知 commutator 标量。
同理它们与第一 $B_{2,Y}$、$\mathsf R_{-1,Y}$ 交换。
二者彼此交换来自完整 CM 纤维重排，单位旋转也保整纤维及全部相位。

## 5. 不删非 principal 角型的有限算术 lift

定义以下固定有限算子，**不附 $\Pi_{0,Y}$**：
$$
\begin{aligned}
\widetilde P_S&=\frac1{18}\sum_{j=0}^{17}(-1)^j\widetilde N_{13}^{\,j},\\
\widetilde P_{\rm new}
 &=\frac{I-\omega\widetilde N_{19}}{36}
       \sum_{j=0}^{17}\omega^{2j}\widetilde N_{13}^{\,j},\\
\widetilde P_H
 &=\frac{I-\omega^2\widetilde N_{19}}{36}
       \sum_{j=0}^{17}\widetilde N_{13}^{\,j}.
\end{aligned}
\tag{15}
$$
本篇不宣称 (15) 在整个第一空间上都是秩一投影。
其余五个第一角型全部留在来源中。

原 first principal 平均严格满足
$$
\boxed{\Pi_{0,Y}\widetilde P_\chi=P_\chi,}
\tag{16}
$$
因为在这个平均后 (12) 的物理单位旋转恒为一。
右边是 R483/R692 已付的完整 S、新曲线、参考投影。

置
$$
e_-=(e_1-e_2)/2,\qquad
\Psi_S=\widetilde P_Se_0,\quad
\Psi_{\rm new}=\widetilde P_{\rm new}e_-,\quad
\Psi_H=\widetilde P_He_- .
\tag{17}
$$
这些是由同一原六输入通过显示的有限 CM 对应得到的固定完整来源。
其第一 principal 分量分别是原 S、新曲线和参考的非零张量，
故没有以零质量代非零来源。

记 $\epsilon_S=1,\ \epsilon_{\rm new}=\epsilon_H=-1$。
原 $e_0,e_-$ 同时满足
$B_{2,Y}e=\epsilon e$、$\mathcal B_Ae=\epsilon e$：
前者是 R692，后者由原 A 三十四层等于 R 的奇次方得到。
再用 (14)，得完整来源身份
$$
B_{2,Y}\Psi_\chi=\epsilon_\chi\Psi_\chi,\qquad
\mathcal B_A\Psi_\chi=\epsilon_\chi\Psi_\chi.
\tag{18}
$$

## 6. 同一个 CM 来源上的三个实际深核

原 whole $K_{136,Y}=R_YB_{2,Y}$。
Z 与第一 Y 正交，第一 CM 算子逐个与其完整 restriction、物理图交换；
R692 的整个 Z 来源式因此可作用于 (17)。
结合 (10)、(18)，得到
$$
\boxed{
\begin{aligned}
\nu_{\Psi_\chi}|_{A\in p^{34}}
 &=\epsilon_\chi\lambda^{34}
       (P_{A,\kappa^{34}})_*\nu_{\Psi_\chi},\\
\nu_{\Psi_\chi}|_{Y\in p}
 &=\epsilon_\chi\lambda
       (R_YP_{Y,\kappa})_*\nu_{\Psi_\chi},\\
\nu_{\Psi_\chi}|_{Z\in p}
 &=\epsilon_\chi\gamma\lambda
       (R_YP_{Z,\kappa})_*\nu_{\Psi_\chi}.
\end{aligned}}
\tag{19}
$$
这是同一个未删角型来源上的三条完整测度等式。
A 端仍是原 A，未更换为 R695 的 $A_s$。
Y/Z 两个物理反射仍保留。
没有由此推出 W 核与 (15) 交换。

对任意由这三个真实物理映射组成的正词 M，
若 A/Y/Z 字母数分别为 a,b,c，则准确为
$$
\boxed{
\nu_{\Psi_\chi}|_{M\mathcal O^6}
=\epsilon_\chi^{a+b+c}\gamma^c
 \lambda^{34a+b+c}M_*\nu_{\Psi_\chi}.
}
\tag{20}
$$
这是真像格；任何另附原条件必须按整个 M 转置。
(20) 不把不同物理词按其相同来源标量作商。

## 7. 仍是原 q♯、原三条已识别曲线行

$N\in4\mathbf Z_{>0}$，固定 R679 的实际 $q_N^\sharp$。
它与第一 Y 的 CM、角平均和单位旋转交换。
在完整 Y-unit 测试
$f_w(Y)=1_{Y\ {\rm unit}}\langle Y\rangle^{d_pw}$ 下，
可以在**返回后**使用 (16)，因为 $f_w$ 为 principal。
由 R692 的原完整行，准确有
$$
\boxed{
\int q_N^\sharp f_w(Y)\,d\nu_{\Psi_\chi}
=\lambda^N
\begin{cases}
J_S(w),&\chi=S,\\
\frac{52}{3}\langle2\rangle^{-d_pw}J_{\rm new}(w),&\chi={\rm new},\\
c_H\langle2\rangle^{-d_pw}J_H(w),&\chi=H,
\end{cases}}
\quad
c_H=-\frac{1+\delta}{2016b}.
\tag{21}
$$
两个 $2^{-1}$ 仍是物理 Y 与 theta 轴 $2Y$ 的原尺度。
$J_H(0)=1+\lambda$，未知参考导数保留。

把 (20) 与 (21) 合并，给同一实际词域上的完整返回
$$
\boxed{
\int_{M\mathcal O^6}
 (q_N^\sharp\circ M^{-1})\,f_w(Y\circ M^{-1})\,d\nu_{\Psi_\chi}
=\epsilon_\chi^{a+b+c}\gamma^c\lambda^{34a+b+c+N}
 \mathcal J_\chi(w),
}
\tag{22}
$$
其中 $\mathcal J_\chi$ 是 (21) 三行中相应的固定曲线函数。
三原中央失败只消这里的 S、新曲线中央；
没有给参考行或它的质量赋零。
原 T 行仍按 R692/R695 在其完整词/观察范围使用。

与 R695 不同，(22) 在每个来源上是**同一个未经 CM 共轭的原词域**。
代价是来源使用 (15) 的全部角型、A 需要三十四层、
测试必须按显示的 M 全部返回。
这不是把 (15) 改成 $P_\chi$ 后在原词域直接积分。

### 7.1 A 门和有限多项式的准确范围

用 R695 的
$$
H=D^*+a_0A+b_FQ+\ell_0L=D^*-E/29,\qquad
a_0=-(5+6\omega)/29,\quad g=3-2\omega.
$$
在 A 单字返回时
$$
\Delta_{34}=a_0(\kappa^{-34}-1)A,\qquad
\mathbf X=(H/\kappa^N,H+14C,13H_1+g(H+C)).
$$
实际返回权是
$$
\boxed{
1_{C\ {\rm unit},\,H+\Delta_{34}\in p^N}\,
 \mathcal P_N\bigl(\mathbf X+\Delta_{34}(\kappa^{-N},1,g)\bigr).
}
\tag{23}
$$
在 $A\in p^{N+34}$ 上，两 H 门相同，完整差准确是
$$
1_{C\ {\rm unit},\,H\in p^N}
 \sum_{\ell=1}^{12}\frac{\Delta_{34}^\ell}{\ell!}
 (\kappa^{-N}\partial_1+\partial_2+g\partial_3)^\ell
 \mathcal P_N(\mathbf X).
\tag{24}
$$
在 $34\le v_p(A)<N+34$，两个 H 门严格不交。
因此 (24) 不适用于该浅部分，两个完整权管都须保留。
对原 R678 角域 $A\in p^{2r},Q\in p^k\mathcal O^\times,L\in p^n\mathcal O^\times$，
若 $2r\ge N+34$ 且 $2r-34>k$，返回 Y 仍在原 k 环带，
但有限差 (24) 仍存在。这没有免费继承原角域另一个来源上的非零值。

## 8. 为什么不能把 Π0 提前穿过 A 深条件

完整算子 (11) 与第一角平均并不交换。
在 first $\mathcal S_{136}$ 的 Schrödinger 模型中，
取 $v=e_0-e_{68}$。它在第一 E[2] 的两个标准生成元上具有
字符 $(+,-)$，且第一反射固定 v。
在第二 $\mathcal S_{19720}$ 取相同 E[2] 字符的非零 w。
则 $\mathcal B_A(v\otimes w)=v\otimes w$。

第一 $\omega$ 旋转把三个非零 E[2] 字符循环置换，
而第二字符保持不变。因此
$$
\mathcal B_A(R_\omega v\otimes w)=-R_\omega v\otimes w,\qquad
\mathcal B_A(R_\omega^2v\otimes w)=-R_\omega^2v\otimes w.
$$
三个第一字符子空间互异，故它们的和非零。
在反射偶部分，$\Pi_0=(I+R_\omega+R_\omega^2)/3$，从而
$$
\boxed{
[\mathcal B_A,\Pi_{0,Y}](v\otimes w)
=-\frac23(R_\omega v+R_\omega^2v)\otimes w\ne0.
}
\tag{25}
$$
所以 (16) 只能在 (21)、(22) 的完整 principal 观察位置使用。
不能把 $\Psi_\chi$ 替换为其第一秩一分量，
然后声称 (19) 仍在相同的原 A 深域成立。
这正是本篇保留全部角型的原因。

## 9. 本结论增加的实际接口

已支付的是一个固定原有限 CM 来源，在旧射线不变时的真实
A 三十四层/Y/Z 三轴共同核心，以及其全部未共轭词域的
原 S、新曲线、参考行 (22)。
它把 R695 中一部分依赖 CM 分支的管族，换成同一完整来源上的原 A 管；
没有消去 W/V 混管，未重新解释任何未知补域。

要继续控制原非零角域，仍须把 (23) 的 H 门和十二次差、
实际 W 失败支、以及 (25) 保留的非 principal 联合分量完整接回。
原三中央并未因此自动矛盾，主目标仍未完成。

## 公开复现

独立程序
[check-r698-adjusted-cm-and-thirty-four-layer-return.js](../scripts/check-r698-adjusted-cm-and-thirty-four-layer-return.js)
已随公开运行请求登记。完整正文先按规则12发布，未等待复跑。
默认运行：
$$
\texttt{node scripts/check-r698-adjusted-cm-and-thirty-four-layer-return.js}.
$$
程序读取零数据文件，输出仅摘要和确定性散列；
不生成入库证书，不依赖网络或第三方包。
按规则13在公开 Actions 执行，本稿没有在会话 V8 运行它。
真实 run ID 和输出 SHA256 由主线程登记。

程序核旧 CRT 的完整 17² 剩余、阶 17、三十四次 whole ratio、
固定张量 Gram、全部 N_A 个 Schrödinger 指标、两个 adjusted CM 的
完整二挠 lift 和 (25) 的有限字符证据。
来源归属、非零锚、整测度及全部算术量词由正文证明。

依赖：
[R410](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)；
[R487](R487-original-cm-mixed-tubes-and-common-core-reference-carry.md) 及其 CRT 程序；
[R500](R500-original-pure-y-axis3699-and-complete-w-depth-complement.md) 及其 new_ray 合并；
[R503](R503-original-unit-annuli-and-single-shallow-boundary.md)；
[R522](R522-common-degree3-even-factor-and-same-st-positive-test.md)；
[R488](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)；
[R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)；
[R679](R679-neutral-degree-twelve-three-s-and-exterior-return.md)；
[R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)；
[R695](R695-original-cm-word-domains-and-a-z-carries.md)。
