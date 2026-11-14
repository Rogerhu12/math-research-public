# R119 续篇：保持酉性的全高外消元、两侧 Poisson 与真实角投影缓冲

2026-11-14，visible-exact / tail_connector。

**状态：解析证明，供独立审查。** 本篇在原完整 root-Airy 波振幅
空间中重新组织已付高网络，使高投影成为一个真正酉网络的正交
压缩。原第Z束的非酉行操作可用于解方程，却不能直接拿来使用酉
Schur 恒等式；本篇用同一个 unitary 同时共轭行和列，避免该问题。

对原阈值
$$
 T_i=2^{65536}\lambda_i^4
     =2^{65664}(j+5)^2\delta_j^{-9}
$$
以上的所有内部端口，高外方程保留全部低输入、mean、外端口和
源。其两侧真正 Poisson 算子 $E_H,F_H$ 满足
$$
 \boxed{\quad
 \|v^{\pm1}E_Hv^{\mp1}\|,\quad
 \|v^{\pm1}F_Hv^{\mp1}\|<2^{-9000},
 \qquad
 v_j=2^{-432000}(j+5)^{-4165}\delta_j^{1073/32}.
 \quad}                                                     \tag{H.1}
$$
这是 $L^2$ Hilbert 端口范数，不把高外 inverse 的一阶损失删掉。
$v$ 严格来自五盒谱权 (Q.28)，在中频上 $v\le\mathcal W$。

完整低 Schur 仍是酉的，所有 affine 源按原有序式保留。
真实坐标中的投影与原物理 Fourier cutoff 之间还给一个明确的
双倍缓冲门。这里**没有**把低 Schur 称为已反演，也没有把尚未
消去的无限低尾和有限浅前缀包含在 (H.1) 的“高外”名称中。

## 1. 同一原网络和两个真实基础窗

采用
[完整负散射及网络 word](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
(W.35)--(W.50) 和
[固定标量正常形](R119-supplement-fixed-scalar-normal-form-and-slope-unit-high-network.md)
(Z.1)--(Z.29) 的同一真实 $\Gamma^*(\mathbf a,\Omega)$。
物理角周期为 $\pi/2$，$m=4n$。定义
$$
 g=4/3,\qquad \lambda_i=2^{32}\sqrt{j+5}\,\delta_j^{-9/4}.
 \tag{H.2}
$$

在全部已覆盖的内部 root-Airy incoming 上，原完整网络是
$$
 I-U_a,\qquad U_a=R_+S_- .
$$
$S_-$ 和 $R_+$ 都是完整双端酉算子，包含 positive cross、两个
mean 与所有角模。开口外边界作为输入/输出端口保留：可把
真实 partial wiring 写成相同 Hilbert 端口空间上的酉 colligation，
但不对这些外口施加一个虚构的反射或方程。
下文在所有未覆盖外口上置 $P_H=0$。

第W束给明确的模型
$$
 S_-^{(1)}=\begin{pmatrix}0&B^*\\C&0\end{pmatrix},
 \qquad B=M_B,\quad C=M_C ,
 \tag{H.3}
$$
其中每个分支、每个角锥上的 $B,C$ 都是真正 unitary。
从 (W.48)--(W.50) 读取
$$
 I-U_a=I+S_-^{(1)}+\mathcal E^{\,w},\qquad
 \|\mathcal E_i^{\,w}:H^0\to H^g\|,
 \quad
 \|\mathcal E_i^{\,w}:H^{-g}\to H^0\|
 <2^{9020}\lambda_i^g .                                  \tag{H.4}
$$
两门包含相邻全部输入列；其 adjoint 的高输出门由第二式给出。
全部所需行列度数不超过8。有限外端口继续按其已付源 norm 消费。

第Z束对正角锥的
$V_+=-C^*B$、负角锥的 $V_-=-B^*C$，已构造相应 unitary
$\mathcal W_\pm$，其正逆 $H^r$ norm小于4、$|r|\le2$，
并且
$$
 \widetilde V_\pm=\mathcal W_\pm^*V_\pm\mathcal W_\pm
          =\mathcal U_\pm^0+\mathcal R_\pm ,
$$
$$
 \|\mathcal R_\pm:H^0\to H^g\|,
 \quad\|\mathcal R_\pm:H^{-g}\to H^0\|
                         <2^{4500}\lambda_i^g .           \tag{H.5}
$$
$\mathcal U_+^0$ 的非mean Fourier 值是
$e^{i(n\omega_i+\beta_i^0/n)}$，负锥使用原真实共轭约定。
没有更换任何实际主相位或首密度相位。

## 2. 真正共同酉共轭

在正锥取
$$
 T_+=\operatorname{diag}(I,C),\qquad
 H_+=T_+\operatorname{diag}(\mathcal W_+,\mathcal W_+).
$$
直接相乘：
$$
 T_+^*S_-^{(1)}T_+
     =\begin{pmatrix}0&B^*C\\I&0\end{pmatrix}
     =\begin{pmatrix}0&-V_+^*\\I&0\end{pmatrix}.            \tag{H.6}
$$
在负锥则取
$$
 T_-=\operatorname{diag}(I,B),\qquad
 H_-=T_-\operatorname{diag}(\mathcal W_-,\mathcal W_-),
$$
于是
$$
 T_-^*S_-^{(1)}T_-
       =\begin{pmatrix}0&I\\B^*C&0\end{pmatrix}
       =\begin{pmatrix}0&I\\-V_-&0\end{pmatrix}.            \tag{H.7}
$$
这些锥分块采用原 polar unitary 模型；真实跨锥部分在 (H.4)
中完整保留。mean 上 $H_i=I$。所以其 direct sum $H$ 是满射酉。

令
$$
 \widehat U_a=H^*U_aH,\qquad
 U_d=\begin{cases}
 \begin{pmatrix}0&(\mathcal U_+^0)^*\\-I&0\end{pmatrix},
                    &\text{正锥},\\[2mm]
 \begin{pmatrix}0&-I\\\mathcal U_-^0&0\end{pmatrix},
                    &\text{负锥}.
 \end{cases}                                             \tag{H.8}
$$
mean 的模型取原负交换 $-P$，只为使 $U_d$ 在完整空间酉；
真实 mean 方程不由此替换。
$U_d$ 在非mean上按原层和 Fourier 对角。

这里每个 $T_i$ 在 $|r|\le g$ 的正逆 norm小于 $2^{64}$；
连同 $\mathcal W_\pm$，$H_i^{\pm1}$ 的该 norm小于 $2^{66}$。
在 forward 强窗只对左因素 $H^*$ 收高阶费，右因素只收
$L^2$ unitary；在反向基础窗顺序相反。
因此 (H.4)--(H.7) 给
$$
 \widehat U_a=U_d+\mathcal R,\qquad
 \boxed{\quad
 \|\mathcal R_i:H^0\to H^g\|,
 \quad\|\mathcal R_i:H^{-g}\to H^0\|
                          <2^{12000}\lambda_i^g .
 \quad}                                                     \tag{H.9}
$$
最大的原指数为 $9020+66$；加入 (H.5)、两行、角锥和有限
相邻计数仍小于9100。这里采用12000是明确余量，不是调用
一个未经识别的通用符号常数。两个端点窗的 Hilbert 插值覆盖
$-g\le s\le0$ 的 $H^s\to H^{s+g}$。

与旧 (Z.31) 不同，(H.8) 是同一个 unitary 的真正共轭。
因此其正交高压缩和低 Schur 可以使用准确 Green/酉恒等式。

## 3. 原高算术除法和全部层权

原第Z束 (Z.34)--(Z.36) 已证明
$$
 N_i<2^{160}J^3\delta^{-13/2},\qquad T_i>4N_i,\qquad
 |1+e^{i(n\omega_i+\beta_i^0/n)}|^{-1}
                         <2^{10}\langle m\rangle
 \quad (|m|\ge T_i).
 \tag{H.10}
$$
它使用尾部原两相位的完整整数证明，不借其它 finite head 的
旋转数间隙。对正锥，
$$
 (I-U_d)^{-1}
   =(I+(\mathcal U_+^0)^*)^{-1}
      \begin{pmatrix}I&(\mathcal U_+^0)^*\\-I&I\end{pmatrix},
$$
负锥的对应式为
$$
 (I+ \mathcal U_-^0)^{-1}
      \begin{pmatrix}I&-I\\\mathcal U_-^0&I\end{pmatrix}.
$$
于是 $D_0=I-P_HU_dP_H$ 在高块上满足
$$
 \|D_{0,i}^{-1}f_i\|_{H^s}
                  <2^{12}\|f_i\|_{H^{s+1}}.               \tag{H.11}
$$
$P_{H,i}=\mathbf1_{\{|m|\ge T_i\}}$；
所有 mean 和未覆盖外口属于 $P_L=I-P_H$。

本节允许任一只依赖层的正权 $w_i$，满足每个真实相邻块
$$
                 2^{-256}\le w_i/w_k\le2^{256}.          \tag{H.12}
$$
每行/列至多8个块，且相邻 $\lambda$ 比小于64。
用 (H.9) 的全部强输出，不先截输入，有
$$
 \|w^{\pm1}D_0^{-1}P_H\mathcal R P_{H,L}w^{\mp1}\|
  <2^{12000+12+256+32}\,
                       T_i^{-1/3}\lambda_i^{4/3}
  <2^{-9500}                                             \tag{H.13}
$$
于 $\ell^2_iH^s$，$-g\le s\le0$。
这里 $T_i^{-1/3}\lambda_i^{4/3}=2^{-65536/3}$；
显示的32 bits 包含 $\langle m\rangle/|m|$、两行、
相邻尺度和 Hilbert 块 Schur 行列计数。
同一式对 $\widehat U_a^*-U_d^*$ 成立，来自 (H.9) 的第二窗。
特别没有用只有单个 forward 窗的余项来支付另一侧 Poisson。

所需真实谱权正好满足 (H.12)。五盒篇 (Q.28) 给
$v_i\le\mathcal W_{i,m}$ 于实际中频，而
$$
 v_j=2^{-432000}J^{-4165}\delta_j^{1073/32},\qquad
 \frac{v_j}{v_{j+1}}
   =2^{1073/32}(1+1/J)^{4165}.
 \tag{H.14}
$$
于全部 $j\ge129$，$J\ge134$，其相邻比小于 $2^{80}$；
距离至多2的块比小于 $2^{160}$，严格在 (H.12) 内。
有限外端口可用相邻第128层的同一明确权，仍只改变其已知输入
单位，不替它添加内部方程。
$v^{-1}$ 同样满足 (H.12)。这是从已选择 $\mathcal W$ 导出的
较小权，未重置为更有利的旧 $\delta$ 权。

## 4. 真高 inverse：保留一阶源损失

把 $\widehat U_a$ 按 $P_L,P_H$ 分块为
$$
                 \widehat U_a=\begin{pmatrix}A&B\\C&D\end{pmatrix}.
 \tag{H.15}
$$
$C=P_H\mathcal R P_L$，$B^*=P_H\mathcal R^*P_L$，
因为模型 $U_d$ 与两个投影准确交换。
由 (H.13)，
$$
 I-D=D_0(I-\Theta),\qquad
 \Theta=D_0^{-1}P_H\mathcal R P_H,\qquad
 \|w^{\pm1}\Theta w^{\mp1}\|<2^{-9500}.
 \tag{H.16}
$$
因而对于真实高源 $g_H\in\ell^2H^{s+1}$，准确存在唯一
$x_H\in\ell^2H^s$：
$$
 R_Hg_H=(I-\Theta)^{-1}D_0^{-1}g_H,\qquad
 \|w^{\pm1}R_Hg_H\|_{H^s}
                        <2^{14}\|w^{\pm1}g_H\|_{H^{s+1}} .
 \tag{H.17}
$$
只在 $-g\le s\le0$ 的已付窗声称此式。
$R_H$ **没有**因此成为一个有界的 $L^2\to L^2$ 全源 inverse。

对零源齐次方程也没有漏掉其它 $L^2$ 解：若 $(I-D)x=0$，
则由 (H.9) 得 $D_0x=P_H\mathcal R x$；右端已在局部
$H^g$ 中，故可在分布意义下作准确 Fourier 除法，得到
$x=\Theta x$，由收缩得 $x=0$。
同样证明适用于 $I-D^*$。

## 5. 两侧真正 Poisson 都是 L2 小算子

定义高外的输入 Poisson
$$
 E_H=R_H C
       =(I-\Theta)^{-1}D_0^{-1}P_H\mathcal R P_L .
 \tag{H.18}
$$
它的 source $C x_L$ 已有完整 $4/3$ 阶增益，所以 (H.13)
直接给
$$
                \|w^{\pm1}E_Hw^{\mp1}\|<2^{-9499}.        \tag{H.19}
$$
这是 $L^2_L\to L^2_H$ 的真实解，含所有 mean 和全部低输入；
没有假定该输入是一个预先局部化的 incoming 包。

对 adjoint 的整个高方程应用同一证明，得到
$$
 F_H^*=(I-D^*)^{-1}B^*,\qquad
                \|w^{\pm1}F_H^*w^{\mp1}\|<2^{-9499}.
$$
对偶并交换 $w,w^{-1}$，得到同样的
$F_H:L^2_H\to L^2_L$ 界。对于 $H^1$ 的真实高源，
$$
                         F_Hg_H=BR_Hg_H .                \tag{H.20}
$$
其有界 $L^2$ 延拓来自上述 adjoint 构造，不是擅自将 $R_H$
的定义域扩大。放宽即得 (H.1)。

这同时证明准确 intertwining
$$
 (I-D)E_H=C,\qquad F_H(I-D)=B,\qquad
                      B E_H=F_H C.                      \tag{H.21}
$$
最后一式先在光滑低输入上按 (H.17) 证明，再由完整有界
延拓得到。所有 high/low 交叉块都参加这些式子。

## 6. 完整低 Schur 的酉性、所有源与 mean

定义
$$
                    S_L=A+B E_H=A+F_H C .                \tag{H.22}
$$
给任意 $x_L\in L^2$，向量 $(x_L,E_Hx_L)$ 在高行上准确
固定，且
$$
 \widehat U_a\binom{x_L}{E_Hx_L}
              =\binom{S_Lx_L}{E_Hx_L}.
$$
完整酉性给 $\|S_Lx_L\|=\|x_L\|$。
对 $\widehat U_a^*$ 和 $F_H^*$ 重复同一证明，得到
$S_L^*=A^*+C^*F_H^*$ 也等距。因此 $S_L$ 满射酉。
此处没有要求一个不存在的有界 $L^2$ 高 resolvent。

原完整有源方程
$(I-\widehat U_a)(x_L,x_H)=(g_L,g_H)$ 准确化为
$$
 (I-S_L)x_L=g_L+F_Hg_H,\qquad
 x_H=E_Hx_L+R_Hg_H .                                     \tag{H.23}
$$
$g_H$ 要按 (H.17) 提供一阶更强的 norm，以保证实际高解；
仅将有界延拓 $F_Hg_H$ 写进低方程，不赋予高解额外正则性。

若最外端口只是 colligation 的输入/输出，并未被施加方程，
(H.22)--(H.23) 按相同 block 消元读取其中实际内部行和外输出。
这保留全部外响应，不将外部擅自闭成一个固定反射。

原 source 先按真正次序变成 $\widehat g=H^*g$。
这里不再应用旧 (Z.31) 的非酉行矩阵。
$g$ 必须是原 root/Piola、strict total-density、完整 positive
total-DN 和 graph 法向负荷所得的 source；原 mean 电荷、独立
高度、bare flux 所需端点迹均继续保留。
两列 $D\Gamma^*$、metric-source 和当前端图微分也按同一个
$H^*$ 进入。若微分 $H^*$，准确多出
$\dot H^*g$ 及相应状态坐标项；本固定背景结果不使它们为零。

## 7. 径向右 Poisson 的局部频率阈值费用

后续实际-minus-radial Schur 差中的右 Poisson 是径向的。
它逐 Fourier 对角，所以可比 (H.19) 多保留一项有用信息：
$$
 \Omega_i(m)=\max\left(1,\frac{\langle m\rangle}{1+T_i}\right).
 \tag{H.24}
$$
低输入上 $\Omega=1$；相邻层的 $\Omega_i/\Omega_k$ 小于
$2^{20}$。与 (H.14) 合成后，$(v\Omega)$ 的相邻比仍小于
$2^{256}$。

对径向对象，所有被共轭的块仍逐 Fourier 对角，
因此逐频重复 (H.13)--(H.19)，再求 Hilbert 直和，给
$$
 \boxed{\quad
 \|\Omega_Hv^{\pm1} E_{H,0}v^{\mp1}\|<2^{-9000}.
 \quad}                                                     \tag{H.25}
$$
这是允许随频率变化的空间权，因为此处算子确实径向。
没有把 (H.25) 未经证明地授予实际非径向 $E_{H,a}$。

由于 $\langle m\rangle<2T_i\Omega_i(m)$，(H.25) 表示：
右 Poisson 虽把一个低输入带到较浅层的高区，仍可以按其所在
那一层的 $T_i$ 支付一次角导；跨越多层产生的 $M/T_i$ 因子
已由真实 high 反馈几何和吸收。不能先将所有层的 $T_i$ 取
一个不存在的全局 supremum。

具体地，若以后从同一 root 波单位获得
$\Delta\widehat U_i:H^1\to L^2$ 的逐层小量 $\epsilon_i$，
则正确 Schur 差使用
$$
 S_{L,a}-S_{L,0}
    =\begin{pmatrix}I&F_{H,a}\end{pmatrix}
       (\widehat U_a-\widehat U_0)
       \binom I{E_{H,0}} .
 \tag{H.26}
$$
(H.1),(H.25) 真正支付这里两侧高外响应。
但原 $Q=7$ 单位中的差不能直接代成
$\Delta\widehat U$；其 root 端口、真实 $H$ 及下节投影仍须
按实际公式转换。

## 8. 真实角表示与双倍频率缓冲

这里给一个明确的 projection 门，避免将 (H.8) 的 Fourier
截断误认成原物理角截断。
第Z束的实际角费用仍为
$$
 \epsilon_i^c=2^{8192}J^{16}\delta_j^{-16}
                    (N_j^c)^\#\mathcal X,\qquad
 \sum_i\lambda_i\epsilon_i^c<2^{-18918}.                   \tag{H.27}
$$
令 $\chi\in C^1(\mathbb R)$ 为固定实偶函数，
$0\le\chi\le1$、$\chi=0$ 于 $|\xi|\le1$、
$\chi=1$ 于 $|\xi|\ge2$、$\|\chi'\|_\infty\le4$。
对任何 $L\ge4$，同一实际 unitary $H_i$ 满足
$$
 \|[\chi(D_\theta/L),H_i]\|_{L^2\to L^2}
         <\sigma_i:=2^{10000}\lambda_i\epsilon_i^c,
 \qquad \sum_i\sigma_i<2^{-8918}.                         \tag{H.28}
$$

给出其来源，尤其不对尖 cutoff 作错误的小差断言。
原 signed-density 图是
$\Lambda^{-1/2}\mathcal D_K\Lambda^{1/2}$，mean 独立保留。
沿真实实微分同胚路径 $K_s$，其 generator 是
$\Lambda^{-1/2}\partial_\theta M_{v_s}\Lambda^{1/2}$，
$ v_s=\dot K_s\circ K_s^{-1}$，至号数不影响以下 norm。
第Z束 (Z.6),(Z.8) 的完整角域与角 Cauchy 费用给
$\sum_\ell|\ell||\widehat v_s(\ell)|<2^{2048}\epsilon_i^c$。

非mean的 commutator 矩阵条目包含
$$
 [\chi(m/L)-\chi(n/L)]\sqrt{|mn|}\,
                              \widehat v_s(m-n).
$$
准确有
$$
 |\chi(m/L)-\chi(n/L)|\sqrt{|mn|}
                                      \le32|m-n|.        \tag{H.29}
$$
若 $m,n$ 同号且可比，非零差迫使它们在 $L$ 附近，使用
Lipschitz 门；若不可比或异号，则
$\sqrt{|mn|}\le2|m-n|$。mean 相关列按原真实有限秩项另保，
由同一 Fourier moment 支付。整个行列和因而由
$32\sum|\ell||\widehat v_s(\ell)|$ 控制。
沿 $K_s$ 的两个真实同阶端因素、角锥压缩和 polar 校正一起
可收在 $2^{6144}\epsilon_i^c$ 内：polar 的误差和 cross 采用
第W束 (W.18) 已付20阶门，其 norm和 commutator均小于该数。

模型的 radial phase 因素与 $\chi(D/L)$ 准确交换；
其非mean角系数、首次同调及相应 selfadjoint exponent 的差，
由 (Z.15),(Z.19) 的有序 Duhamel 小于
$2^{2050}\lambda_i\epsilon_i^c$。
沿模型中有限且少于32个因素使用 commutator 乘积公式，
所有其余因素只在 $L^2$ 上收费1，便得到更宽的 (H.28)。
没有将径向大首相位放进一个巨大指数，也没有对径向 $C^4$
支集求额外高导数。

因此有真正的分隔频带门
$$
 \|P_{\ge2L}H_iP_{\le L}\|,
 \quad\|P_{\ge2L}H_i^*P_{\le L}\|<\sigma_i .               \tag{H.30}
$$
第一式等于
$P_{\ge2L}[\chi(D/L),H_i]P_{\le L}$；
第二式由 adjoint commutator 给出。
mean 在 $H_i$ 下准确不移动，其实际网络 high 耦合仍留在
(H.18)，不是从这里被删除。

原波表示中的真正高投影是
$H P_HH^*$。尖 cutoff 在同一阈值处的差一般不能由 (H.28)
估成小量；后续接原物理 Fourier 包必须保留 $[L,2L]$ 的
缓冲带，或准确使用这个共轭投影。
(H.30) 不授予一条未经转换的 $Q=7$ 端口结论。

## 9. 尚待闭合的外部和原强空间

本篇实际完成了完整高外的双向解、两个 $L^2$ Poisson、
相邻层权、全 source 公式和投影缓冲。均保留全部 mean 和低输入，
不要求 whole-network 近核先进入一个猜测的 incoming 低锥。

剩下的 $P_L$ 仍含各层 $|m|<T_i$，其中包括真实无限 low-tail
和可能未属于高窗的有限浅前缀。原低尾强解与其 affine 允许线、
全部 current $\Gamma^*$ 列、普通/weak源原标签权还须实际连接；
不能因第5节的高外闭合而把这些项叫作高块的一部分。

五盒篇的径向谱选择在原 $Q=7$ 端口，
[完整物理网络差](R119-supplement-complete-physical-Q7-network-difference-and-weighted-middle.md)
也在该单位。本篇在原 root-Airy 波单位，二者之间的真实
root/strict/graph map及共轭须按其完整 norm 接合。
最终 $\mathcal F=0$ 和课题完成标准尚未由本篇证明。
