# R258 — 原二处运输后的完整对数 monodromy 与非恒定交换差

日期：2026-11-13。**状态：原共轭 CM17 迹、共同 $[2]$、$\mathcal V$ 和 $Q_{+,v}$ 后的对数系数已按真实 theta 群算出。十六个 ray 角色的非恒定对数部分仍线性独立；其二阶运输交换差也有明确非零的十五阶对数系数。没有据此断言原三条中央导数非零。**

本篇直接计算 [R253](R253-four-octic-ray-logarithms-and-norm2-constants.md)
的对数来源经 [R246](R246-third-dyadic-bidirectional-cm17-and-complete-central-bridge.md)
原运输后还剩什么。其四个八次角色包含在下面的十六角色结论中。
本文使用的是原变系数 theta 分支；没有把它们换成裸 ray 常数，
也没有把混合二处、十七处的挠点值归入纯八挠单位域。

## 1. 实际来源、共同尺度和对数系数

保持原规范
$$
E_0:y^2=x^3-x,\qquad dz=dx/(2y),\qquad
\beta=4-i,\quad\bar\beta=4+i,
$$
$$
S_8=-y\vartheta\sigma^3,\qquad F=S_8^{17},\qquad
r(z)=\frac{x(z)-1}{x(z)+1}.
$$
$F$ 的次数为 $68$，线丛具有 $T_0=(1+i)\Omega_0/2$ 扭转。
在实际复覆盖上，它的整周期半特征是
$$
F(z+\omega)=(-1)^{m+n}
\exp\!\left(\frac{68\pi\bar\omega}{\Omega_0^2}
                  (z+\omega/2)\right)F(z),
\qquad \omega=(m+ni)\Omega_0.                              \tag{1}
$$
从本节起 $\pi$ 表示式 (1) 中的实圆周率；本篇没有使用 norm-five
素元 $2+i$，因而没有二者混淆。

固定 $P_{17}\in E_0[\beta]\setminus\{O\}$。
对 $\mathbf F_{17}^{\times}$ 的任一角色 $\chi$，令
$$
\Psi_\chi(w)=
\sum_{a\in\mathbf F_{17}^{\times}}\chi(a)^{-1}
                        \log r(w+aP_{17}),\qquad
\Phi_\chi=\Psi_\chi-\Psi_\chi(0).                         \tag{2}
$$
这里也容许平凡角色。对四个八次角色，(2) 正是 R253 的原对象。

取共轭 CM17 的实际有限平坦迹并作共同 $[2]$：
$$
\boxed{
\mathcal L_\chi(z)=F(2z)
\operatorname{Tr}_{\bar\beta w=2z}
 \left[\frac{F(\beta w)}{F(\bar\beta w)}\Phi_\chi(w)\right].
}                                                        \tag{3}
$$
这与 R248、R254 的 frame 一致，次数为 $272$。
每个分支均使用 (1) 确定的比值；不省略迹中不同周期代表的指数。

本文把局部展开中的 $\log(z-z_*)$ 系数记作
$\operatorname{res}^{\log}_{z_*}$。复解析延拓绕该点一周时，增量为
$2\pi i$ 乘这个系数。这里的系数一般是一个完整的解析 germ，
不是它在奇点处的值；有高阶零的非零 germ 仍给非零对数增量。
该记号也可在代数对数连接中使用。
原 $p$ 进 germ 的任意恒等式必须保持这一形式对数系数：
除去共同 theta frame 后，所有分支系数在一个固定有限椭圆覆盖上
为代数函数，而 $\log r$ 是这些函数的对数原函数。
等价地，可把一个假定关系所涉及的有限个常数嵌入复数域，
保持其代数 Taylor 递推，再比较上述解析延拓。
因此本篇不使用一个未经定义的 $p$ 进拓扑 monodromy。

原除子为
$$
\operatorname{div}r=2(T_+)-2(T_-),\qquad
T_+=\Omega_0/2,\quad T_-=i\Omega_0/2.                    \tag{4}
$$
所以 (3) 的对数点在
$2z=\bar\beta(T_\pm-aP_{17})$。
不同 $a$ 的点不会因二原挠平移而相撞：一个非零十七挠点不能是
二原挠点。每个点在原十七重迹中恰有一个对数分支。

## 2. 原 $\mathcal V$ 的准确十六项稀疏展开

令
$$
P=\frac{\beta\Omega_0}{16},\qquad Q=-iP,\qquad
\xi=e^{\pi i/16},\quad\zeta=\xi^2,
$$
并使用 R246 的实际次数 $272$ 平移
$$
\mathcal T_t f(z)=
\exp\!\left(\frac{272\pi\bar t}{\Omega_0^2}z
          -\frac{272\pi|t|^2}{2\Omega_0^2}\right)f(z-t).
                                                               \tag{5}
$$
写 $X=\mathcal T_P,Z=\mathcal T_Q$，则
$ZX=\zeta XZ$、$X^{16}=Z^{16}=1$，且
$$
\mathcal T_{aP+bQ}=\xi^{-ab}Z^bX^a.                     \tag{6}
$$
这些关系用于对数系数模单值来源的商时仍准确成立。

R246 的四项算子实际是自伴的：
$$
\begin{aligned}
\mathcal R^*=\mathcal R
 &=\frac{ZX+\zeta Z^{-1}X+\zeta ZX^{-1}+Z^{-1}X^{-1}}
          {1+\zeta}\\
 &=\frac1{2\cos(\pi/16)}
       \sum_{\epsilon,\eta=\pm1}\mathcal T_{\epsilon P+\eta Q}.
\end{aligned}                                                   \tag{7}
$$
因此，连同 R246 的全部归一常数，
$$
\boxed{
\mathcal V=2^{-3/8}\Pi_0
       \sum_{\epsilon,\eta=\pm1}\mathcal T_{\epsilon P+\eta Q},
\qquad
\Pi_0=\frac1{16}\sum_{a,b=0}^3X^{4a}Z^{4b}.
}                                                               \tag{8}
$$

自然次数 $1156$ 的来源 $F(\beta w)\Phi_\chi(w)$ 具有同一 $T_0$ 扭转；
$[\bar\beta]_*$ 保持它，因为 $\bar\beta T_0=T_0$。
作 $[2]$ 后，对数系数满足
$$
X^8\mathcal L_\chi=-\mathcal L_\chi,\qquad
Z^8\mathcal L_\chi=-\mathcal L_\chi
\quad\text{模单值来源}.                                  \tag{9}
$$
在标准 $p$ 进有理函数对数的周期代换中可直接使用准确等式；
即使采用复路径记账而增加一个水平 frame 常数，它的对数系数为零，
不改变 (9)。

(7) 的每个奇、奇平移把两个符号同时变成正。
在该像上
$$
\Pi_0=\frac14(1+X^4)(1+Z^4).
$$
于是 (8) 对原对数系数的完整稀疏展开为
$$
\boxed{
\mathcal V=
\frac{2^{-3/8}}4
\sum_{\epsilon,\eta=\pm1}\sum_{a,b=0}^1
 (-1)^{ab}\xi^{4(b\epsilon-a\eta)}
 \mathcal T_{(\epsilon+4a)P+(\eta+4b)Q}.
}                                                               \tag{10}
$$
这里不是把一个完整高维矩阵按采样截断。精确脚本在有限 Heisenberg
代数中验证：原 (8) 的六十四项与 (10) 的十六项之差，右乘
$(1-X^8)(1-Z^8)/4$ 后为零。

## 3. 在一个实际输出点只剩两个分支

固定标签 $a\ne0$，选复覆盖代表
$$
z_a=-\bar\beta aP_{17}/2,\qquad
s=\epsilon P+\eta Q,\qquad
z_*=z_a+s+4P+4Q.                                         \tag{11}
$$
在输入端，两个对数点可分别取为 $z_a+4P$、$z_a+4Q$。
精确的周期修正是
$$
\bar\beta T_+-8P=i\Omega_0,\qquad
\bar\beta T_--8Q=4i\Omega_0.                              \tag{12}
$$
令 $\omega_+=i\Omega_0,\omega_-=4i\Omega_0$，定义实际分支系数
$$
\boxed{
m_\pm(z)=
\frac{F(2z)}{F(2z+\omega_\pm)}
F\!\left(\frac{\beta}{\bar\beta}(2z+\omega_\pm)\right).
}                                                               \tag{13}
$$
(13) 中的比值由 (1) 延拓为非零指数；它不是一次未确定的 frame
归一。原对数系数在两点分别为
$2\chi(a)^{-1}m_+$、$-2\chi(a)^{-1}m_-$。

在 $P,Q$ 坐标模八中，输入两组点分别为 $(4,0)$、$(0,4)$。
(10) 的四对 $(\epsilon,\eta)$ 在模四中互异。
因此在 (11) 的输出点，只有两个准确平移有贡献：
$$
t_+=s+4Q,\qquad t_-=s+4P.                               \tag{14}
$$
它们分别对应 (10) 中 $(a,b)=(0,1),(1,0)$。
其他标签不会混入这个点，其他两个平移的输入点也不在 (4) 的除子上。

置
$$
g_+(z)=\mathcal T_{t_+}m_+(z),\qquad
g_-(z)=\mathcal T_{t_-}m_-(z),
$$
$$
v_+(z)=\frac{\beta}{\bar\beta}
                     (2z-2t_++\omega_+).
$$
则直接从 (10)、(13) 得
$$
\operatorname{res}^{\log}_{z_*}(\mathcal V\mathcal L_\chi)
=2^{-11/8}\chi(a)^{-1}
       \left(\xi^{4\epsilon}g_+-\xi^{-4\eta}g_-\right).
                                                               \tag{15}
$$
所有真实变系数仍在这两个 $g_\pm$ 中。

## 4. 两分支的完整比值和非零十七阶系数

本节把 (15) 的两个 Gaussian 全部相除。其两个 $F$ 自变量之差为
$$
D=\beta(T_--T_+)
  =\frac{-3+5i}{2}\Omega_0
  =T_0+(-2+2i)\Omega_0.                                 \tag{16}
$$
R251 的真实半周期式为
$$
\mathcal T^{68}_{T_0}F=-iF x^{-17}.
$$
(16) 多出的整周期，其半特征和相应乘法相位都为一。
所以也有 $\mathcal T^{68}_{-D}F=-iF x^{-17}$。

把 (1)、(5)、(13) 逐项代入，两个指数的 $z$ 系数准确消去；
常数指数为 $(68\pi/\Omega_0^2)C_{\epsilon,\eta}$，其中
$$
C_{\epsilon,\eta}
 =\frac{i(-17\epsilon-17\eta-268)}{16}\Omega_0^2.
$$
加上 $\omega_+,\omega_-$ 的相反半特征，结果是
$$
\boxed{
\frac{g_-(z)}{g_+(z)}
 =-i\,\xi^{-4(\epsilon+\eta)}x(v_+(z))^{-17}.
}                                                               \tag{17}
$$
这里的比值是实际 meromorphic germ 的比值；不是只比较最低项。
完整有理相位的四个值为

| $(\epsilon,\eta)$ | (17) 中 $x(v_+)^{-17}$ 的系数 |
|---|---:|
| $(-1,-1)$ | $1$ |
| $(-1,1)$ | $-i$ |
| $(1,-1)$ | $-i$ |
| $(1,1)$ | $-1$ |

代回 (15) 即得到本篇的明确公式：
$$
\boxed{
\operatorname{res}^{\log}_{z_*}(\mathcal V\mathcal L_\chi)
=2^{-11/8}\chi(a)^{-1}\xi^{4\epsilon}g_+(z)
       \left(1-i\epsilon\eta\,x(v_+(z))^{-17}\right).
}                                                               \tag{18}
$$
若采用 R254 的 $\mathcal L_\chi/b_\chi$ 归一，右端整体再除以同一个
已知非零 $b_\chi$；没有其他改变。

在 (11) 的点，准确有
$$
v_+(z_*)=\beta T_+-\beta aP_{17},\qquad
x(v_+(z_*))=-1.                                          \tag{19}
$$
$S_8$ 在 $T_-$ 是简单零，故 $g_+$ 恰有十七阶零。
而 (18) 最后一个因子的值为
$$
1+i\epsilon\eta\ne0,\qquad
(1+i\epsilon\eta)(1-i\epsilon\eta)=2.                    \tag{20}
$$
所以 (18) 的对数系数**准确仍为十七阶非零 germ**。
在零点处把 $g_+$ 的值代成零，会错误删除这个实际对数分量。

## 5. 全十六角色的原运输没有消去非恒定对数

取全部角色 $\chi_j(3)=\zeta^{\,j}$，$0\le j\le15$。
假设常数 $c_j$ 使
$$
\sum_jc_j\mathcal V\mathcal L_{\chi_j}
$$
变成单值的 theta 来源，包括有限个固定对数常数乘单值来源的情形。
在每个 (11) 的点比较 (18)，其共同变系数由 (19)–(20) 非零，得到
$$
\sum_{j=0}^{15}c_j\chi_j(a)^{-1}=0
\qquad\text{对每个 }a\in\mathbf F_{17}^{\times}.
$$
原十六乘十六 Fourier 矩阵满足
$\mathcal F\overline{\mathcal F}^{\,t}=16I$，所以全部 $c_j=0$。
因此
$$
\boxed{
\dim\langle\mathcal V\mathcal L_{\chi_j}\rangle
 \quad\text{模单值来源}=16.
}                                                               \tag{21}
$$
尤其 R253 的四个八次 primitive 在此商中仍线性独立。
这和全纯正权 theta 的五维像并不冲突：含对数的来源不属于那一个
有限全纯截面空间。

进一步，R231 的真实八项算子满足
$$
Q_{0,+}Q_{+,0}=\Pi_0.
$$
其实际展开是
$$
\begin{aligned}
Q_{+,0}&=\tfrac14\{(M^2-1)(N+N^3)-(M+M^3)(1+N^2)\},\\
Q_{0,+}&=-\tfrac18\{(1+M^2)(N+N^3)+(M+M^3)(1-N^2)\}.
\end{aligned}
$$
共同 $[2]$ 后的 $M,N$ 及其所有相位仍按 R246 使用。
这些是有限 theta 群的代数恒等式，故也作用于本文的对数系数；
不需要延长 R248 的 norm-five 十六次幂关系。
由于 $\mathcal V=\Pi_0\mathcal V$，如果
$Q_{+,0}\mathcal V$ 消掉某个非零组合的对数系数，再作用
$Q_{0,+}$ 就与 (21) 矛盾。于是
$$
\boxed{
\dim\langle Q_{+,v}\mathcal L_{\chi_j}\rangle
 \quad\text{模单值来源}=16,\qquad Q_{+,v}=Q_{+,0}\mathcal V.
}                                                               \tag{22}
$$
此处既保留了实际八项运输，也保留了 (18) 的非恒定系数。
没有仅凭一个常数矩阵的秩，把对数来源当成全纯来源。

## 6. 原二阶来源的真实交换差必含非零对数项

令
$$
\mathcal F(w)=F(\beta w),\qquad
\nabla_\beta=\partial_w-\mathcal F'/\mathcal F,\qquad
\nabla_2=\partial_z-F(2z)'/F(2z).
$$
原二阶来源满足
$$
\nabla_\beta^2(\mathcal F\Phi_\chi)
=\mathcal F\Phi_\chi''.
$$
它全局全纯：$\Phi_\chi''$ 至多有二阶极点，而 $\mathcal F$ 在所有
这些点的零重至少十七。定义其实际运输
$$
\mathcal K_\chi
=\mathcal V\left(
 [\bar\beta]_*(\nabla_\beta^2(\mathcal F\Phi_\chi))(2z)\right).
                                                               \tag{23}
$$
因此 $\mathcal K_\chi$ 没有对数系数。
对非平凡 $\chi$，它正是原有理 ray 二阶来源的 $-8$ 倍运输；
平凡角色另有已经明确的常数 frame 项。

把 (23) 中同一个完整算子写成实际分支和：
$$
\mathcal V\mathcal L_\chi=\sum_\nu a_\nu(z)\Phi_\chi(w_\nu(z)),
\qquad w_\nu'(z)=2/\bar\beta,
$$
其中 $\nu$ 遍历原 (8) 的六十四项平移及十七个 trace 分支。
这里使用完整 (8)，所以所有水平常数也被保留。
$a_\nu$ 准确由 (1)、(3)、(5) 给定。
置
$$
A_\nu=\partial_z\log(a_\nu/F(2z)).
$$
链式法则给出完整等式
$$
\boxed{
\begin{aligned}
\mathcal K_\chi={}&
\frac{\bar\beta^2}{4}\nabla_2^2(\mathcal V\mathcal L_\chi)\\
&-\bar\beta\sum_\nu a_\nu A_\nu\Phi_\chi'(w_\nu)\\
&-\frac{\bar\beta^2}{4}
 \sum_\nu a_\nu(A_\nu'+A_\nu^2)\Phi_\chi(w_\nu).
\end{aligned}
}                                                               \tag{24}
$$
每个系数都是原同一分支的系数；没有把 $A_\nu$ 任意设为零。

在 (11) 的点，$F(2z)$ 非零，因为该点具有非零十七原部分，而
$F(2z)$ 的零点全为二原挠点。因此 $\nabla_2$ 在此正则。
(18) 恰有十七阶零，所以其二阶协变微分的对数系数恰为十五阶，
首项乘以
$$
17\cdot16\ne0.                                           \tag{25}
$$
故 (24) 后两行的和必有一个相反的、**非零的十五阶对数系数**，
才能与全纯的左端相容。
这给出原交换差的实际非零证书：它不能被有限个固定对数常数乘
单值 theta 来源替代。对全部十六角色，这些系数的 Fourier 矩阵仍
是 (21) 的矩阵，所以常数线性组合也不能将它们全部消去。

## 7. 与 R255 完整中央观察的准确接口

对 R248 的三种四次角色，$B_k=-\Phi_{\lambda^k}''/8$，因而
$$
T_k=
-\frac1{8b_k}[\bar\beta]_*
       \bigl(\nabla_\beta^2(\mathcal F\Phi_{\lambda^k})\bigr).
                                                               \tag{26}
$$
把 (26) 再接 R250 的 $\operatorname{adj}(A)$、真实二处算子及
R255 的完整参考商，就是该篇的 $Y_B$ 分布观察。
因此 (24) 是其对数 primitive 方向的一条具体运输公式。
它没有声称 Mellin 泛函与任意一个微分或平移交换。

R253、R256 提供的固定单位对数仍可用于 (24) 中准确保留下来的
常数部分；(18)、(24) 说明其余部分实际存在。
如果要把 R255 的二阶观察等同于一个有限固定对数线性型，仍须处理
这些明确的非恒定分支及其完整移权。本文没有用常数的线性独立，
取代这一步算术比较。

## 精确证书

[脚本](../scripts/check-ray-log-dyadic-monodromy.py) 与
[输出](../scripts/check-ray-log-dyadic-monodromy.json) 在特征零准确核验：

- 原半特征上的六十四项到十六项等式、全部实际平移坐标及相位；
- (12)、(16) 的整周期修正和 (17) 全部 Gaussian 的线性项消去；
- 四个剩余常数相位、(18) 的完整 $x^{-17}$ 因子及其非零首项；
- 每个选定输出点恰有两个分支，以及原十六角色 Fourier 可逆性。

全程保留稀疏 theta 群结构，没有构造大稠密矩阵，也没有从目标素数
样本外推。解析与除子证明见本文 (1)–(26)，所用原半周期恒等式为
R251 (5)、(8)，其余规范同 R246、R248、R253。
