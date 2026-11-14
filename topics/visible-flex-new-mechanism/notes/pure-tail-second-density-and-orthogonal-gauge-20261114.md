# pure 幂尾下一阶：准确第二 density 与正交 profile 规范

日期：2026-11-14。独立纸面研究补记；不占新结果号。本稿给出可用于 R85 后阶分析的准确规范与一个第二 history 的下一系数。**没有证明 pure 第四 $4m-8$ 项消失，也没有给第四成本符号。** 正在运行的 tail producer 源码保持冻结。

## 1. 共同约定

沿用 R73/R85，令

$$z=\xi+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
e_s=h_s z-h\omega_s,\quad \lambda=e_s/h^2,$$

$$K_0=kz^2-(k^2+1)z/h,\qquad K=K_0+\lambda_s,\qquad\omega_s=k_s/(2h).$$

所有 $s$ 导数固定 $\xi$。正右尾为

$$J_e(f,g)=\int_\xi^r\{(1+e(s,\eta)^2)f''g''+2h^2 f'g'\}\,d\eta.$$

$f,g$ 暂为不依赖 $s$ 的静态 profiles，在共同右 collar 为零。R73 原二阶密度记为 $r_s(f,g)$，下标表示真实几何位置。

## 2. 清除第二 density 显式速度项的准确规范

定义对称局部算子

$$\boxed{\Lambda_s(f,g)=
-\frac{h_sQ}{8h^3}f'g'
-\frac{e_s}{8h^3}J_e(f,g).} \tag{1}$$

若 $W_s=r_s(f,g)$，令 $\widehat W=W-\Lambda_s(f,g)$。则

$$\boxed{\begin{aligned}
\widehat W_s={}&\frac{ke}{2}fg
-\frac{kQ}{4h}(fg'+f'g)\\
&+\frac{K_\xi Q}{8h}f'g'
+\frac{K}{8h}J_e(f,g).
\end{aligned}} \tag{2}$$

### 逐项证明

R73 的 $fg$ 与对称 $fg'$ 系数已经分别是 $ke/2$ 与 $-kQ/(4h)$，(1) 的 $s$ 导数不产生这两种局部项。其原 $f'g'$ 系数为

$$\frac{K_{0,\xi}Q}{8h}
-\frac{h_s e e_s}{4h^3}+\frac{h_s^2Q}{8h^4}.$$

加入 $\partial_s(h_sQ/(8h^3))$ 后，两个 $h_s e e_s$ 项抵消，余下

$$\frac Q{8h}\left(K_{0,\xi}+\frac{h_{ss}}{h^2}-\frac{2h_s^2}{h^3}\right)
=\frac{K_\xi Q}{8h},$$

因为 $\lambda_\xi=h_s/h^2$。

对尾项，用 $d=h\omega-k$，$J_e=(1+d^2)J_0+2hdJ_1+h^2J_2^*$。R73 的三个尾系数，加上 $\partial_s(e_sJ_e/(8h^3))$ 后，逐项分别成为

$$\frac K{8h}(1+d^2),\qquad \frac{Kd}{4},\qquad \frac{Kh}{8}.$$

例如 $J_0$ 系数中的 $-2e_s d d_s/(8h^3)$ 与导数产生的相反项抵消；余下的
$K_0/h+e_{ss}/h^3-2h_s e_s/h^4$ 正是 $K/h$。其余两个尾同理。这证明 (2)，没有把 $s$ 总导数当作逐点零。

常值 scalar 端芽上 $h_s=e_s=0$，故 $\Lambda=0$，$\widehat W$ 与原 $W$ 有相同两个端值。这项规范不是改变几何或 profile，只是为真实 history 增加一个明确的局部项。

## 3. 一个 profile 随 s 变化时保留的链式项

令外 profile $f$ 静态，内 profile 为 $g(s,\xi)$。R73 的真实链式公式是

$$R[H(Y_f,Y_{g(s)})]=r_s(f,g)+\Psi_s(f,g_s),$$

$$\Psi_s(f,v)=\Lambda_s(f,v)-\frac{b_s}{4}f'v,
\qquad b=d/h=\omega-k/h.$$

这里 $b_s=kh_s/h^2-\omega_s$。因此令 $\widehat W=W-\Lambda_s(f,g(s))$ 后，准确有

$$\boxed{\widehat W_s=\widehat r_s(f,g)-\frac{b_s}{4}f'g_s,} \tag{3}$$

其中 $\widehat r$ 是 (2) 右侧的静态双线性式。证明必须同时微分 (1) 的几何系数和 $g$；后者产生 $\Lambda(f,g_s)$，恰与 $\Psi$ 的对称部分抵消。

式 (3) 只声称一个输入静态的情况，不冒称两个输入同时变化时没有新的二次时间导数项。它适用于后续把一个实际恢复场拆成 $Y_{g(s)}$ 与余场后的该部分，不能用它删除余场。

## 4. 第二 history 的下一幂系数

取 R85 的单位幅值尾 $q=t^m$，$t=c-\xi$，$m\ge8$，置 $p=2m-3$。定义

$$\mathcal C(s,c)=\frac{K(s,c)Q(s,c)}{8h},\qquad
\mathcal D(s,c)=\frac{K(s,c)e(s,c)}4.$$

写

$$\widehat W_2=b_0(s,c)t^p+b_1(s,c)t^{p+1}+O(t^{p+2}).$$

由 (2) 直接得到

$$b_0'=\frac{m^2(m-1)^2}{2m-3}\,\mathcal C,$$

$$\boxed{b_1'=
-\frac{m^2(m-2)^2}{2m-3}\,\partial_c\mathcal C
-\frac{m^2(3m-5)}{2(2m-3)}\,\mathcal D.} \tag{4}$$

这里 $\partial_c\mathcal C$ 是同一实际几何在查询右端的 $\xi$ 导数，不改变右锚或路径。

为核对 (4)，令 $A_m=m^2(m-1)^2$。右尾积分有

$$J_e(q,q)=A_m\left(\frac{Q_0}{p}t^p-\frac{2he_0}{p+1}t^{p+1}\right)+O(t^{p+2}).$$

$fg$ 与 $fg'$ 两局部项从 $t^{p+3},t^{p+2}$ 才开始。因此 $t^{p+1}$ 的系数恰为

$$\left(m^2-\frac{A_m}{p}\right)\frac{K_\xi Q_0}{8h}
-\frac{A_m}{p+1}\frac{Ke_0}{4}.$$

使用 $K_\xi Q_0/(8h)=\partial_c\mathcal C-\mathcal D$，得到 (4)。这个下一系数仍只是第二 history 的真实 ODE，不是第四 period 的结论。零二阶总矩阵会使 $b_0,b_1$ 在两个常值端芽都回到零，但不能因此把它们在整个路径内部设零。

## 5. 任意恢复场的准确正交分解

对 R56 任意恢复场，保留原数据

$$Z=\frac Fz\left(A,zP+B,eA-hW\right),\qquad
A=\frac{W_\xi}{2}+\frac{\eta_0}{h}.$$

此节 $F$ 是移动 frame，$B$ 是 R56 的局部分子配对，均不表示 profile 目标。记有符号右原函数 $I(f)=\int_r^\xi f$。定义一个实际、可随 $s$ 变化的 profile

$$\boxed{\psi=W+2Q\,I\left(\frac{\eta_0}{hQ}\right).} \tag{5}$$

则有准确场分解

$$\boxed{Z=-Y_\psi+\frac Fz\left\{
(zP+B)(0,1,0)
+\frac{h(\psi-W)}Q(-e,0,1)\right\}.} \tag{6}$$

括号内的余分子逐点垂直于 $(1,0,e)$，不是仅在最低阶或样本点正交。

**证明。** 第一、三分量在 $(1,0,e)$ 方向的投影为

$$QA-ehW=\frac Q2W_\xi-ehW+\frac Qh\eta_0.$$

而 $-Y_\psi$ 分子的相应投影是 $Q\psi_\xi/2-eh\psi$。因 $Q_\xi=2he$，

$$\frac Q2\psi_\xi-eh\psi=\frac{Q^2}{2}(\psi/Q)_\xi.$$

式 (5) 使两个投影准确相等。剩余切向方向 $(-e,0,1)$ 与 $(1,0,e)$ 正交，其平方长为 $Q$。原分子在该方向的内积为 $-hW$，$-Y_\psi$ 为 $-h\psi$，故余系数为 $h(\psi-W)/Q$。中间分量原样保留，得到 (6)。

式 (5) 一般含新的右 Volterra 积分及 $1/Q$，不等于上一节只针对双齐次场的 $W-\Lambda$。不能凭最低项相同就把这两个完整规范互换。

## 6. 正交规范的端项必须怎样使用

一般路径的 (5) 在两端可有非零局部修正；它没有 R85 的 $W+\lambda P$ 那种仅凭常值 germ 就逐阶端修正为零的性质。

有一个明确的充分条件可保 period：考虑相同 scalar 常值端芽的环，第二和第三的完整 scalar histories 在末端都等于起始值。原 R56 是按阶三角系统；在同一个几何常值 germ 与相同低阶 histories 下，由各自真实 RHS 求出的所需有限阶 $s$ jets 也相同。因此第二、第三、第四 forcing 的 $P,B,\eta_0$ 在两端一致。

第四 forcing 不含第四未知 history；它只由已经匹配的第一至第三场及其导数组成。故 (5) 中第四局部修正的两个端值一致，得到

$$\psi_4(L,\xi)-\psi_4(0,\xi)=W_4(L,\xi)-W_4(0,\xi). \tag{7}$$

第二、第三也有对应端差身份。其正交 profile 在起点却可能不为零，必须保存这一初值，不能改成逐阶“重新零锚”。$M=\mathcal T=0$ 的同态环提供上述低阶端值匹配；两个不同 scalar 端口的开桥不能直接套用 (7)。

## 7. 对第四下一阶尚能与不能断言的事

(2) 清楚给出第二 history 到下一幂的准确 ODE，(6) 则给完整的 profile 部分与正交余场。正交性可能消除某些最高阶交叉项，但余场的 $s,\xi$ 导数仍会进入 R56，动态 profile 的链式项也仍在 (3) 中。尤其不能因两个场分子正交，就宣称其导数张量的全部 forcing 为零。

因此目前未由这些公式证明 $4m-8$ 的完整 period 消失。正在执行的公开 tail producer 将提供原始全 histories 系数；下一步应把它与上述规范和正确初末局部项逐项对照，再证明任何额外的总导数或残余。没有在本地编译或求值真实研究目标，也没有由倒行偶性推断第四成本正性。
