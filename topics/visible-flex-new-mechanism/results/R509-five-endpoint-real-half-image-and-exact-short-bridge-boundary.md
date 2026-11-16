# R509：完整 ruling 内的五端实际半像与短段矩阵复位的准确边界

日期：2026-11-16。**新的完整纸面构造；没有执行 profile 求积、符号程序、秩、数值优化、开发检查或科学任务。**

[R508](R508-nonzero-second-gauge-opens-secant-exit-and-two-sided-matrix-port.md) 已从一条真正支付了完整 ruling 的参考正割打开非正割出口：同一个字面母库、固定第二规范 $w_\theta=B D_\theta$ 和固定第三规范 $\chi_\theta$ 沿整段不变，终端 $k,\omega$ 可以复位，而原 $p_2$ history 可以小幅取两号。本稿不将这个单读出误写成完整八矩控制。

新增实际结论是：仍在这同一个受约束路径族中，可准确指定
$$
k(L)=0,\quad\omega(L)=\omega_0,\quad
m_{p_0^y}(L)=0,\quad m_{p_2}(L)=0,\quad
m_{p_1^y}(L)=\eta
\tag{1}
$$
对每个充分小的 $\eta>0$ 成立。五端映射在每个充分小的非零构造点是真实 submersion，故在这些点附近还有三个 $p$ 坐标的完整开像。其余五个矩阵坐标、高度、frame、位置和第三、第四成本均来自同一条实际路径，仍未复位。

这个半像的单侧性也能准确解释。对原真实路径，$m_{p_1^y}$ 有一个不使用 ruling 的完整 Volterra 恒等式。它使整个足够短的统一控制盒上 $m_{p_1^y}\ge0$，非恒 $k$ 时严格正。因此不能把本稿的局部开像或两个相反控制参数误作全矩阵零桥。最后给出任何从这种 scalar 起点出发的真 $M=0$ 段必须离开的明确量化范围。

## 1. 固定同一实际状态、同一规范和原八矩坐标

本稿只消费 R508 已完成的一次选择：字面同形实偶紧母、原十矩和八／十二／五块包装、一个固定正割参数 $H$、固定 $B=P-cR_y$，以及一次选定的 $\chi_\theta$。所有 profile、幅度、中心和右锚都不再随本稿端点目标改变。

参考轨道的真实 scalar 是
$$
h_{\rm sec}=H\sec\sigma,\qquad
\sigma=s+\sigma_0,\qquad
v=\tan\sigma,\qquad
k=0,\quad\omega=\omega_0 .
\tag{2}
$$
取一条固定短子段 $[0,L]$，使
$$
0<\sigma_0<\sigma_0+L<\pi/4 .
\tag{3}
$$
R508 的完整能量偏导在这条参考轨道邻域非零，因而已给光滑反馈
$$
\gamma=h_s=G_B(h,k,\omega,\mathsf m,\upsilon),
\qquad\upsilon=k_s ,
\tag{4}
$$
以及真实 ODE
$$
h_s=G_B,\qquad k_s=\upsilon,\qquad
\omega_s=\frac{\upsilon}{2h},\qquad
\mathsf m_s=M_{\rm raw}(h,k,\omega,G_B,\upsilon).
\tag{5}
$$
全部相位的完整第四 ruling 在(5)上为零；原二、三阶 ruling 仍由同一母库支付。真实第三、第四恢复、frame 和位置继续随(5)积分，不在子段入口重新置零。

这里的入口历史来自参考正割中心的真实积分。尤其三个 $p$ history 在参考正割上为零；其它历史一般不为零。所有控制都严格内支撑，所以新路径保留参考子段完整的真实左 germ。

为明确固定坐标，写
$$
y=x+\omega_0,\qquad \bar\omega=\omega-\omega_0,\qquad
d_y=h\bar\omega-k.
$$
R73 的原局部系数 $A_1=p_0+p_1x+p_2x^2$ 在这个一次固定的坐标中是
$$
A_1=p_0^y+p_1^y y+p_2^y y^2,
$$
其中
$$
p_0^y=p_0-\omega_0p_1+\omega_0^2p_2,\qquad
p_1^y=p_1-2\omega_0p_2,\qquad p_2^y=p_2.
\tag{6}
$$
因此以下是真实八矩的三个固定线性坐标，不是沿路径重新变基。原 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(9)准确给
$$
\boxed{
(M_{\rm raw})_{p_0^y}=-\frac{k(1+d_y^2)}{2h},\quad
(M_{\rm raw})_{p_1^y}=k^2-kh\bar\omega,\quad
(M_{\rm raw})_{p_2}=-\frac{kh}{2}.
}
\tag{7}
$$
若从起点选 $\omega_0=0$，(6)就是原字面 $p_0,p_1,p_2$。一般固定 $\omega_0$ 时，(1)在原 $x$ 坐标等价于
$(m_{p_0},m_{p_1},m_{p_2})=(\omega_0\eta,\eta,0)$，不能省去这个坐标关系。

## 2. 四个终端读出可在同一完整 ruling 中一起指定

对一个光滑内支撑控制变分 $\delta\upsilon=\psi$，在参考轨道有
$$
k_1(s)=\int_0^s\psi(t)\,dt,\qquad
\omega_1(s)=\int_0^s\frac{\psi(t)}{2h_{\rm sec}(t)}\,dt .
\tag{8}
$$
高度变分在第二式中乘参考 $\upsilon=0$，故不出现。三个 $p$ 的一阶式由(7)直接得出：
$$
\begin{aligned}
\delta m_{p_0^y}(L)
&=-\frac12\int_0^L\frac{k_1(s)}{h_{\rm sec}(s)}\,ds,\\
\delta m_{p_1^y}(L)&=0,\\
\delta m_{p_2}(L)
&=-\frac12\int_0^Lh_{\rm sec}(s)k_1(s)\,ds .
\end{aligned}
\tag{9}
$$
这里也没有遗漏高度项：它们分别乘参考 $k=0$；$d_y^2$ 对 $p_0^y$ 没有一阶贡献。

定义四端映射
$$
\mathcal F(\upsilon)=
\bigl(k(L),\bar\omega(L),m_{p_0^y}(L),m_{p_2}(L)\bigr).
\tag{10}
$$
交换真实有限积分后，其微分是对控制 $\psi$ 的四条权：
$$
\begin{aligned}
f_1(t)&=1,\\
f_2(t)&=\frac1{2h_{\rm sec}(t)},\\
f_3(t)&=-\frac12\int_t^L h_{\rm sec}(s)^{-1}\,ds,\\
f_4(t)&=-\frac12\int_t^L h_{\rm sec}(s)\,ds .
\end{aligned}
\tag{11}
$$
减去不影响跨度的常数，并乘非零固定尺度，(11)准确等价于
$$
1,\qquad\cos\sigma,\qquad\sin\sigma,\qquad
\log(\sec\sigma+\tan\sigma).
\tag{12}
$$
这四个函数在任意非空参考子区间上线性独立。若
$A+B\cos\sigma+C\sin\sigma+D\log(\sec\sigma+\tan\sigma)=0$，
求一次导数并乘 $\cos\sigma$ 得
$$
-B\sin\sigma\cos\sigma+C\cos^2\sigma+D=0.
$$
$1,\sin2\sigma,\cos2\sigma$ 的原函数关系迫 $B=C=D=0$，再得 $A=0$。这里没有用数值点值或一般性秩猜测。

因此可一次固定四个内支撑光滑控制
$\psi_1,\ldots,\psi_4$，使
$$
\mathcal L_{ij}=\int_0^L f_i(t)\psi_j(t)\,dt
\tag{13}
$$
可逆。具体取四个使(12)点值独立的内点，再取足够小的不交 bumps；连续性保该同一非零 minor。其支撑与端 collar 一次冻结。

有限维 IFT 已经说明：同一真实反馈(5)下，(10)在零控制附近具有实际局部右逆。特别 $p_0^y,p_2$ 可以一起取小两号，同时准确固定终端 $k,\omega$；但此时 $p_1^y$ 与其它五个矩阵坐标随同一控制真实变化，不能删掉。

## 3. 原 $p_1^y$ 有一个完整、非渐近的短段符号身份

下面的引理适用于任何真实 $h>0,k,\omega$，不额外借用(4)或 ruling。

假设入口 $k(0)=0,\bar\omega(0)=0$。原
$\bar\omega_s=k_s/(2h)$ 直接积分给
$$
\boxed{
\bar\omega(s)=\frac{k(s)}{2h(s)}
+\frac12\int_0^s k(t)\frac{h_s(t)}{h(t)^2}\,dt .
}
\tag{14}
$$
这是对 $k/(2h)$ 的真实分部积分。没有在 $k$ 的零点作除法，也不需要终端 $k,\omega$ 已经复位。

将(14)代入(7)，在零 $p_1^y$ 入 history 下得到
$$
\boxed{
m_{p_1^y}(L)
=\frac12\int_0^L k(s)^2\,ds
-\frac12\int_0^Lh(s)k(s)
  \left(\int_0^s k(t)\frac{h_s(t)}{h(t)^2}\,dt\right)ds .
}
\tag{15}
$$
一般传入值只需在左侧改为真实增量；不把传入历史清零。

令
$$
\mathcal C(h;L)
=L\left(\max_{[0,L]}h\right)
\left\|\frac{h_s}{h^2}\right\|_{L^\infty([0,L])}.
\tag{16}
$$
Cauchy–Schwarz 给
$$
\left|\int_0^Lhk\int_0^s k\,\frac{h_s}{h^2}\right|
\le \mathcal C(h;L)\int_0^L k^2 .
$$
所以准确有
$$
\boxed{
m_{p_1^y}(L)\ge
\frac{1-\mathcal C(h;L)}{2}\int_0^L k^2 .
}
\tag{17}
$$

可以先把参考区间缩短，再固定一个足够小的有限控制参数盒，使该盒内全部实际解统一满足
$$
\mathcal C(h;L)\le\frac12 .
\tag{18}
$$
理由是参考 $h,h_s$ 有固定界，$h$ 有正下界；缩短 $L$ 后(16)小，再由(5)的真实连续依赖保持。四条权(12)在每个非空短区间仍独立，故这个顺序不会破坏(13)。从此 $L$ 固定，所有实际目标使用相同正时长。

在这个实际控制盒中，
$$
\boxed{m_{p_1^y}(L)\ge\frac14\int_0^Lk^2,}
\tag{19}
$$
非恒零 $k$ 时严格正。因而本稿的负 $p_1^y$ 端口不是“尚未从数值找到”：它在这个明确短段范围确实不可达。下面的正端口与此边界相容。

## 4. 在四个准确复位条件的同一纤维上产生正 $p_1^y$

取第五个内支撑 bump，不属于 $\psi_1,\ldots,\psi_4$ 的跨度。用(13)减去它的四个实际线性读出，得到一个非零的紧控制
$$
\psi_*=\widetilde\psi-\sum_{j=1}^4c_j\psi_j,\qquad
D\mathcal F(0)\psi_*=0.
\tag{20}
$$
例如令第五个 bump 支撑与前四个都不交，则相减后仍非零。所有函数是真实、有限、一次固定的光滑函数。

考虑五参数实际控制
$$
\upsilon_{t,z}=t\psi_*+\sum_{j=1}^4z_j\psi_j .
\tag{21}
$$
对每一组小参数，先按同一个(5)求其真实路径，再评价(10)。有限维 IFT 给一个光滑 $z=z(t)$，满足
$$
z(0)=0,\quad z'(0)=0,\qquad
\mathcal F(\upsilon_{t,z(t)})=0.
\tag{22}
$$
因此(22)的所有路径准确保持终端
$k=0,\omega=\omega_0,m_{p_0^y}=m_{p_2}=0$。这是完整非线性复位，非只一阶约束。

令
$$
k_1(s)=\int_0^s\psi_*(t)\,dt,\qquad
\omega_1(s)=\int_0^s\frac{\psi_*(t)}{2h_{\rm sec}(t)}\,dt .
$$
$\psi_*\ne0$ 迫 $k_1\not\equiv0$。由 $z(t)=O(t^2)$ 和原 ODE 的光滑依赖，
$$
k_t=tk_1+O(t^2),\quad
\bar\omega_t=t\omega_1+O(t^2),\quad
h_t=h_{\rm sec}+O(t).
\tag{23}
$$
所有误差在同一紧区间的一次固定光滑范数中统一，未放大或再选择频率。

用(7)的准确二次零阶结构，得到
$$
m_{p_1^y}(t)
=t^2Q_*+O(t^3),\qquad
Q_*=\int_0^L(k_1^2-h_{\rm sec}k_1\omega_1)\,ds .
\tag{24}
$$
其中高度一阶变化只在三次余项中出现；四个 normal 的 $O(t^2)$ 校正也不改变显示的二次系数。

对参考高度应用(14)–(18)，或者直接取(15)的二次系数，准确有
$$
\boxed{
Q_*\ge\frac14\int_0^Lk_1^2>0.
}
\tag{25}
$$
因此每个充分小的 $t\ne0$ 给出同一四复位纤维内的真实正 $p_1^y$ 位移。它不是 signed 响应列，也不把形式平方项当实际有限参数解；完整(22)已经将四个同时端点误差准确消掉。

## 5. 每个小正目标准确可达，非零点的五端映射是 submersion

设
$$
\Phi(t)=m_{p_1^y}(\upsilon_{t,z(t)}).
$$
由(24)，$\Phi(t)/t^2$ 在 $t=0$ 光滑延拓，值为 $Q_*>0$。定义
$$
a=t\sqrt{\Phi(t)/t^2}.
\tag{26}
$$
该函数在零点导数 $\sqrt{Q_*}$ 非零。一次一维 IFT 给光滑反函数 $t=t(a)$，并且
$$
\boxed{\Phi(t(a))=a^2.}
\tag{27}
$$
于是任意充分小的 $\eta>0$ 取 $a=\sqrt\eta$，(21)(22)(27)便给准确(1)。也可取 $a=-\sqrt\eta$ 得另一条真实控制；两个选择的 $p_1^y$ 都是正值，不能把相反控制参数误作相反矩阵目标。

这族在 $a$ 中光滑，在每个 $\eta>0$ 的邻域中也可光滑参数化；本稿不声称存在穿过 $\eta=0$ 的双侧 $C^1$ 右逆。

更强地，令完整五端映射为
$$
\mathcal G(t,z)=
\bigl(\mathcal F(\upsilon_{t,z}),\
m_{p_1^y}(\upsilon_{t,z})\bigr).
\tag{28}
$$
在(22)的某个充分小非零点 $t_0$，前四行对 $z$ 的 minor 仍可逆，而沿其准确零纤维的末行导数是
$$
\Phi'(t_0)=2t_0Q_*+O(t_0^2)\ne0 .
$$
以该四行消元后的 Schur 补正是这个导数。因此
$$
\boxed{\operatorname{rank}D\mathcal G(t_0,z(t_0))=5.}
\tag{29}
$$
不是先算一张形式五列，再将它当成实际端口秩。

其直接后果是：在同一实际路径基准(1)附近，可同时保持终端 $k=0,\omega=\omega_0$，并指定三个 $p$ history 的任意充分小邻域目标。这个邻域位于已经达到的正 $p_1^y$ 基准附近；不包含一个已经被(19)排除的负 $p_1^y$ 目标。

## 6. 完整矩阵与几何基准不能从五端开像中消失

本稿已控制的三个矩阵线性坐标是
$p_0^y,p_1^y,p_2$。原 E8 的其它五个独立坐标仍随同一个真实路径变化。除 trace 关系已经原式保留外，本稿没有让它们自由消失。

此外，以下数据必须一起进入后继的实际词：

- 高度的终值及其完整右 germ；
- frame、中心线位移和共同 $x+\omega>0$ 窗口；
- 完整二阶矩阵的五个余坐标；
- 原第三、第四恢复、传入历史、规范作用及所有 period／十三行基准。

严格内支撑的控制保参考左 collar。终端(1)还使右 collar 上 $k=0,\omega=\omega_0$；三个 $p$ history 在此 collar 均为常数。高度和其它历史继续按(5)真实演化，不由这个结论变成参考右 germ。

所以(1)不是一个“完整八矩只含 $p_1^y$”的纯方向，也不证明该裸段的完整第四成本已经属于只为闭 $M=0$ 词定义的空间。反射、倒行、原桥、prototype 重复与 Klein 合成仍要各自保全部成本；没有 signed 线性组合可以代替这些实际段。

## 7. 为什么同一短盒中的小段不能直接拼成 $M=0$

(19)给出一个准确的后继限制。若本稿短盒中某条路径满足全矩阵增量零，则其 $p_1^y$ 增量为零，故 $k\equiv0$。原方程随即使 $\omega\equiv\omega_0$。

在这固定 $y$ 坐标，R73 的原 $t_1$ 密度在 $k=0$ 时准确为
$$
(M_{\rm raw})_{t_1^y}
=-\frac18\left\{1+\left(\frac{h_s}{h}\right)^2\right\}.
\tag{30}
$$
每个正长度段都有严格负的 $t_1^y$ 增量，因此全矩阵增量仍不能为零。这个推论不依赖本稿特殊的五参数选择，适用于满足(18)且从所列 scalar 起点出发的整个实际短段类。

更一般地，若一条正长度实际路径从 $k=0,\omega=\omega_0$ 出发、全矩阵增量零，则 $k$ 不能恒零；(17)和(30)迫
$$
\boxed{
L\,h_{\max}\left\|h_s/h^2\right\|_\infty\ge1 .
}
\tag{31}
$$
它只是一个必须离开的短段范围，不是一般原 $M=0$ 桥不存在。若后来使用多个短段，只有每段都从同一个所列 scalar 起点复位出发时，(15)才能直接按同一 $p_1^y$ 增量相加；任意不同传入 $\omega,k$ 的桥不能免费套这一号。

因此，(29)已经提供真正的矩阵目标开像，同时(31)说明完整抵消不能仅靠在同一很短的正则盒里堆参数。下一连接必须真实走出这个小盒，或进入不同的已付状态域；仍须在整个连接段保持同一 $w,\chi$ 与完整 ruling。

## 8. 已完成的正向步骤与准确后继

本稿给的是一个固定有限控制族及其准确 nonlinear 端点结论。其必要选择次序为：先固定 R508 的母、规范和参考轨道；再缩短并固定统一段长与控制盒；一次选出四个 normal 和一个真实核方向；用同一个 IFT 支付四复位；最后用(26)实现正的第五目标。全程没有更换母或规范，没有借用无 ruling 限制的 R70 桥，也没有重新给任何先前段赋第三 Gram。

新增结果相较单个 $p_2$ 端口是：三个 $p$ 坐标可以在一个实际正基准邻域同时控制，而该基准本身可以准确落在 $(0,\eta,0)$。局部单侧性与其余五矩、几何和高阶基准均显示保留。

主课题的同一完整周期词、全部端口复位、固定度量有限等距族、闭嵌入和厚度仍未完成。本稿提供继续真实矩阵抵消时可以使用的五端开像，也明确排除了把这个局部开像直接重命名为完整 $M=0$ 控制的做法。
