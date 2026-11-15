# R119 续篇：完整有限 Sobolev 逆的强层衰减与物理平端 C² 重建

2026-11-15，visible-exact / tail_connector。

**状态：已证明；完整有序源的强层衰减，以及实际齐次深尾的物理 C² 延拓。** 本篇接
[1024阶完整网络与物理帽 Schur](R119-supplement-complete-1024-angular-Sobolev-network-and-physical-cap-Schur.md)
U.1--U.28，以及
[闭 mean、兼容与高度 gauge](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)
Z.1--Z.28。对象、共同五盒参数点、两条实际 $\Gamma^*$、
新外根及未匹配的真实接口全部不变。

本篇先在一个明确的原位源空间证明**全部 root 状态**的强层衰减，
包括 actual mean、high、deep-low 和 remaining。
随后对实际深尾无体源、无 weak 源和无原子的解，支付完整
root/strict/positive 的物理二 jet，并得到平端的真正 $C^2$ 延拓。
一般深尾源的端口小量不能代替它的胞内 particular 二 jet；
该额外费用在第9节明确保留。
这也不是原指数 Fourier 标签空间的 inverse 声明。

## 1. 状态、源与主结论

仍写
$$
 \delta_j=(2/25)2^{-j},\quad J=j+5,\quad
 F_j=2^{4096}J^4\delta_j^{-5},\quad
 v_j=2^{-600000}J^{-4165}\delta_j^{1073/32}.
$$
引入本篇证明用层权
$$
       w_j=\delta_j^{-64},\qquad W_p=wF^p,\qquad -3\le p\le3 .
 \tag{D.1}
$$
每个完整负窗的两个 incoming 采用同一层权。原根所属层相差1的
固定缓冲在下面全部计入；没有移动物理根或增设终点条件。
新有限根仍按 U/Z 标为第129层。

原位总源先按 U.25 的准确次序成为
$$
 k_L=g_L+F_Hg_H,\qquad k=k_{\rm rem}+F_Dk_D .
 \tag{D.2}
$$
下文 $k_D$ 是 $k_L$ 的 deep 分量，不是未经 high 消元的
裸输入。所有普通、weak、BV/原子、$\nu$、$D\Gamma^*$、
独立外端口及实际角恢复导数先经过各自已付 source map，
才可代入这些符号。

定义
$$
 \begin{split}
 \mathcal G={}&\|v^{-1}k\|_{\ell^2H^{1024}}
      +\|W_1k\|_{\ell^2H^9}
      +\|W_1k_D\|_{\ell^2H^9}
      +\|W_1g_H\|_{\ell^2H^{10}} .
 \end{split}
 \tag{D.3}
$$
这是完整有序源的一个充分条件，不把任意原物理 $L^2$ 源自动
放进此域。指定高度 $\lambda$ 后，令 $x$ 为 U 的完整增广解，
并从其全部根状态中减去准确物理常高度核 $c_a\lambda$。
则
$$
 \boxed{\quad
       \|W_{-2}(x_{\rm full}-c_{a,\rm full}\lambda)\|_{\ell^2H^8}
                        <2^{1600000}\mathcal G .
 \quad}
 \tag{D.4}
$$
实际全方程仍要求 $\mathcal L_a k=0$；
否则原辅助列的
$\tau=\mathcal L_a k/\mathcal L_a\sigma_\circ$ 明确保留。
本篇没有把这个真实通量荷变成一个自由物理参数。

以下证明只需取 $\lambda=0$。一般情形减去同一个 $c_a\lambda$
即可，不能减去一个假定纯 canonical mean 的向量。

## 2. 新层权确实允许完整高外和 deep-low 消元

在所有 $j\ge129$ 上，(D.1) 的相邻层比及其倒数小于 $2^{80}$；
因为 $F_{j+1}/F_j=2^5((j+6)/(j+5))^4$。
原有限邻接至多跨两层，故实际块比小于 $2^{160}<2^{256}$。
U.17 的**完整**高 Poisson 因而适用于所有这些权。
这控制的是已求逆高外的长程传播；不声称 Schur 后仍有限邻接。

deep 的原径向核在非零 $M=|m|\ge4$ 上准确为
$$
 |R_{D,\circ;jk}(m)|\le F_jF_kq_M^{|j-k|},
       \qquad q_M=2^{-100}M^{-4}\le2^{-108}.
 \tag{D.5}
$$
原文是
[深低完整 Green 与 Poisson](R119-supplement-complete-deep-low-Green-Poisson-and-mixed-elimination.md)
L.14--L.17。原 L.15 显示的 $2^{48}$ 权比在这里**重新**支付：
乘新权后几何比不超过 $2^{-28}$，两端完整行列和仍小于4，
原 $2^{64}$、$2^{128}$ 门都有余量。
第一切口真实允许线、$q_M^{-2}$ 的编号费及两种源跳仍属于
同一个原核，不重新选择低锥。

actual 差仍使用 U.15/U.20；
凡一端在 deep，保留原有序恒等式后才用
$M\le A_j=2^{-40}\delta_j^{-1/8}$。
原 L.21 的 $F^2$ 和一次 $A_j$ 费用，再乘 U 的 $2^{196608}$
角费用及新相邻权费，仍小于 $2^{-6800000}$。
例如第一深行的显示 bits 可宽放为
$50000+196608+160+64\cdot14+58\cdot8197-20010-8388608$，
严格小于 $-7600000$；以后几何余幂大于66。
8192邻胞仍用其原真实第二段 $N_j$，未借深指数。
Neumann 和两个准确 Poisson 差式因此给
$$
 \|W_pF^{-1}R_DF^{-1}W_p^{-1}\|<2^{66},
$$
$$
 \|W_pF^{-1}E_DW_p^{-1}\|,
 \quad\|W_pF_DF^{-1}W_p^{-1}\|<2^{130},
                    \qquad -3\le p\le3 .
 \tag{D.6}
$$
这些结论在本篇所用 $H^s$ 窗成立；径向核逐 Fourier 对角，
actual 的角费用已经由 U 重新付过。
每个公式可先在有限源上证明，再用与穷尽无关的行列和延拓。

## 3. remaining 非mean：由真实频率下界换取层衰减

记 $P_Z$ 为完整 canonical mean 投影，$P_N=I-P_Z$ 于 remaining。
深层 $P_N$ 的实际模式满足
$$
                 M>A_j=2^{-40}\delta_j^{-1/8}.
$$
因此
$$
 {w_j\over v_j}\langle m\rangle^{-1015}
 \le2^{640600}J^{4165}\delta_j^{939/32},
                        \qquad j\ge8193 .
 \tag{D.7}
$$
这里 $1015=1024-9$，余幂准确为
$1015/8-64-1073/32=939/32$。
第一深行可用 $J<2^{14}$；其后相邻比小于 $2^{-28}$。
浅层 $129\le j\le8192$ 另付
$$
 600000+4165\cdot14+(64+1073/32)\cdot8196<1460000
$$
bits，不将浅层当作 deep。故统一
$$
 \sup_{(j,m)\in P_N}{w_j\over v_j}\langle m\rangle^{-1015}
                         <2^{1500000}.
$$
由 U.3，在 $\lambda=0$ 时
$$
                   \|wx_N\|_{\ell^2H^9}
                       <2^{1500001}\mathcal G .
 \tag{D.8}
$$
这里使用的是同一个全混频解；不是逐模另选参数，也没有以
角高频投影代替 actual mean 方程。

## 4. mean 的向外因果 Green 在强层权上有界

Z.11 的 mean Green 从平端向外积分，同时保 height 跳和 flux 跳。
按层编号，它仅在输出 $j\le k$、源 $k$ 的方向非零；
根/窗编号只增加至多两层缓冲。原 Z.15 给
$$
 |R_{Z,\circ;jk}|
 \le2^{4096}J_jJ_k\delta_j^{-4}2^{5(k-j)},\qquad j\le k.
$$
这一向外增长不能改写成一个假衰减 Green。
本篇准确加权后却有
$$
 {w_j\over w_k}F_j^{-1}F_k^{-1}|R_{Z,\circ;jk}|
 \le2^{-4096}J_j^{-3}J_k^{-3}
                       \delta_j^6\,2^{-64(k-j)} .
 \tag{D.9}
$$
$\delta_k^5=\delta_j^5\,2^{-5(k-j)}$ 正好消去旧核中的
$2^{5(k-j)}$。两层缓冲、各层完整根数和 mean 两迹最多增
512 bits。完整行列几何和给
$$
             \|W_{-1}R_{Z,\circ}W_1^{-1}\|<2^{-3500}<1 .
 \tag{D.10}
$$
准确的 $R_{Z,\circ}\sigma_\circ=0$、零高度 gauge 和外自然
零通量仍是 Z.11--Z.14 的物理定义。
不把 strong 层权作为另一个错误的外 Robin 条件。

## 5. actual mean 联立：完整双 Poisson 只收 F³

U/Y 的准确有序恒等式为
$$
 \Delta S_{\rm rem}
  =[I,F_{D,a}]\,[I,F_{H,a}]\,
       \Delta\widehat U\,
       [I;E_{H,\circ}]\,[I;E_{D,\circ}] .
 \tag{D.11}
$$
每个矩阵都作用同一个完整内部压缩，独立外列已在 (D.2)。
径向
$E_{H,\circ}P_Z=E_{D,\circ}P_Z=0$，
因为两被消空间都没有 mean。这是 Fourier 对角参考的准确零式，
不是删除 actual 的 mean/high 或 mean/deep 反馈。

对非mean输入，右侧 deep Poisson 把 $W_0H^9$ 放入
$W_{-1}H^9$，收 $2^{130}$；高 Poisson 保持该权。
左侧为了在 mean 输出取得 $W_1$，deep 左 Poisson 先用
$W_2$，再收 $2^{130}$；高左 Poisson同样保持该权。
所以唯一中间原有限邻接差需要
$W_{-1}H^9\to W_2H^8$，准确只多三份 $F$。

把 U.15 的真实一角导门代入，连这些权和全部邻层，单行可取
$$
 2^{262144}J^{64}\delta_j^{-64}\mathcal N_j\mathcal X .
 \tag{D.12}
$$
其主要账为
$35000+196608+3\cdot4096=243896$ bits，
$J^{40+12}$ 和 $\delta^{-47-15}$；
两侧各130 bits、相邻权、块计数和余两幂均放在显示余量内。
这里完全没有使用 $T_j^\sharp$：输入已经有真实 $H^9$，
一次角导由 $H^9\to H^8$ 支付。
mean 输入的右两 Poisson准确为零，费用更小。

用 U.7 的全部三段 $N_j$，逐段最大值可宽放为
$2^{520000}$、$2^{775000}$、$2^{775000}$。
第三段随后相邻比小于 $2^{-59}$；
有限层数、邻项和两窗计数以后仍有
$$
      \sum_{j\ge129}
         2^{262144}J^{64}\delta_j^{-64}\mathcal N_j
                           <2^{800000}.
$$
新外有限行另为 $2^{480000}(\mathcal X+\epsilon_L)$，
仍用其真实支持129--131；$F$、$w$ 的有限比都已逐项包含。
于是可统一写成
$$
 \|W_1P_Z\Delta S_{\rm rem}P_ZW_{-1}^{-1}\|<\vartheta,
$$
$$
 \|W_1P_Z\Delta S_{\rm rem}P_Nw^{-1}:H^9\to L^2\|<\vartheta,
 \qquad \vartheta=2^{-7500000}.
 \tag{D.13}
$$
不将高消元后的长程 $\Delta S$ 重新当有限邻接；
有限邻接只用于 (D.11) 中间的 $\Delta\widehat U$。

固定 U 已构造的 $x_N$，在 $\|W_{-1}z\|_{\ell^2}$ 中解
$$
 z=R_{Z,\circ}\{k_Z+
        P_Z\Delta S_{\rm rem}(z+x_N)\}.
 \tag{D.14}
$$
(D.10)、(D.13) 给收缩，(D.8) 给其完整非mean强迫，
所以
$$
                         \|W_{-1}z\|<2\mathcal G .
 \tag{D.15}
$$
这个解与 U 的实际 $x_Z$ 相同，不能仅靠形式方程猜测：
新强空间连续嵌入原 $\|vx_Z\|$ 空间，
(D.14) 的源也属于原 $v^{-1}$ 源域。
在原空间，$vR_{Z,\circ}v$ 有界且 U.23 使
$R_{Z,\circ}P_Z\Delta S_{\rm rem}P_Z$ 的 norm小于1。
因此两者之差为零。该识别同时保留 Z 的物理两迹域、
$R_{Z,\circ}\sigma_\circ=0$ 和原真实兼容泛函。

## 6. 全部外消元反向恢复与 compact 根源

由 (D.8)、(D.15)，
$\|W_{-1}x_{\rm rem}\|_{H^8}<2^{1500002}\mathcal G$。
准确反向重建仍是
$$
 x_D=E_Dx_{\rm rem}+R_Dk_D,\qquad
 x_H=E_H(x_{\rm rem}+x_D)+R_Hg_H .
 \tag{D.16}
$$
在 (D.6) 取 $p=-1$，第一项给
$W_{-2}E_Dx_{\rm rem}$，
第二项只需 $\|wk_D\|$，小于 (D.3)。
高外 U.17 再在 $W_{-2}$ 下读取，仍保高源一次角导。
所得完整根状态小于
$2^{1500200}\mathcal G$；放宽即 (D.4)。
其中 high 并没有因 source 在有限频带而被删除。

例如 $\widehat g$ 本身只支于有限层集合 $I_0$，
且 $\widehat g\in H^{1025}$，则 (D.2)、两个完整 Poisson
在相应层权上给
$$
 \mathcal G\le2^{1024}
  \max_{j\in I_0}\bigl(v_j^{-1}F_j^2+w_jF_j^3\bigr)
                     \|\widehat g\|_{\ell^2H^{1025}} .
 \tag{D.17}
$$
(D.17) 已将消元后出现的无限层 source 保留，不误称 $k$ 仍紧支。
$\widehat g$ 是完成真实 source 映射后的根源；
在其之前的物理体源还须满足原 root/Piola/contact 窗。
这里多留的一角阶是充分条件，不是对任意外端 $L^2$ 荷免费补导数。

## 7. 原物理二 jet：三种真片上的自足局部账

本节固定 $j\ge8193$，并假设所讨论的完整深胞及其相邻两胞
没有体源、weak 源或原子。写
$$
 H=\sqrt{\varepsilon_s/\rho}\,h,\qquad
 \widetilde\mu=(\rho/\varepsilon_s)\mu,\qquad
 \widetilde\Lambda=(\rho/\varepsilon_s)\Lambda .
 \tag{D.18}
$$
保持实际 $\rho,\varepsilon_s$。令 $A_j^{\rm in}$ 为该胞所有相邻
完整负窗 incoming 的 $H^8$ norm之和。
U.11 的完整负散射先恢复 outgoing；
再去掉同一个 $H_a$、实际角图和密度架。
对这里最多8阶的角导，U.6 的同一个显式展开只需至多32阶
Fourier moment，全部这些有限转换及逆可保守取 $2^{1024}$。
这含两条 mean，不使用原错误的低频 $b^{1/2}$ 自由架。

下面分别证明，三类实际片共同可取
$$
 \boxed{\quad
   \|H\|_{C^2_{r,\theta}(\text{第 }j\text{ 胞})}
        <2^{131072}J^{12}\delta_j^{-32} A_j^{\rm in}.
 \quad}
 \tag{D.19}
$$
本式只需原径向 $C^4$ profile 所已有的导数；
没有因角阶1024而索取1024阶径向导数。

### 7.1 严格负段：原密度两 mean 和 raw PDE

使用
[真实 strict 密度](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
S.5--S.22、S.28--S.41 及负完整 word W.23。
以 $\mathcal W_8=(c,\alpha,|D|^{-1/2}Z_+,|D|^{-1/2}Z_-)$
为完整平衡状态，单根至 strict 的实际前缀和 strict 内部演化可取
$$
        2^{4096}\lambda_j^{5/3},\qquad
        2^{2048}J^5\delta_j^{-10},\qquad
        \lambda_j=2^{32}\sqrt J\,\delta_j^{-9/4}.
 \tag{D.20}
$$
这是 W.23 的单根前缀，未乘两次整个负段。
径向各频 multiplier 与角权交换；actual 8阶差仍按 U.9
作一次完整 Duhamel。有限角费用包含在这里增出的 bits 中。

准确密度恢复是
$$
 w_d=c+\alpha(S_+-S_-)
       -i\sum_{\sigma=\pm}C_{S_\sigma}D_\theta^{-1}Z_\sigma,
 \qquad
 (w_d)_t=d(w_d)_\theta+\nu\zeta,\qquad
 H=\widetilde\Lambda^{-1/2}w_d .
 \tag{D.21}
$$
这里 $w_d$ 是密度高度，不是层权 $w$；
$\zeta=\mathcal D_{S_+}(Z_++\alpha)-
\mathcal D_{S_-}(Z_--\alpha)$。
两条 mean 的独立行就是原 S.17，未以 $c$ 冒充实际平均高度。

控制 profile 的 C.6、$1\le r\le2$、
$q=\sqrt Q>1/16$、$D<2$ 和 $m_j\ge\delta_j^6$ 给
$$
 \widetilde\Lambda={m_jp_*\over r^8}{q\over D}
                          >2^{-14}\delta_j^7 .
$$
原真实 slope bounds 给
$q<2^8\sqrt J\,\delta_j^{-3/4}$、
$|Q_t|<2^{64}J\delta_j^{-3}$。
用 S.9--S.10 与
$\partial_t\log\Lambda=-1-Q+Q_t/(2Q)-D_t/D$，
所需至多6阶角 multiplier均可取
$$
 \widetilde\Lambda^{-1/2}<2^8\delta_j^{-7/2},\qquad
 |\partial_t\log\Lambda|_{H^6}<2^{100}J\delta_j^{-3}.
$$
(D.21) 于是控制 $H,H_\theta,H_{\theta\theta},H_t,H_{t\theta}$。

二阶径向导数不用对这个较坏的 density导数再微分。
原无源 raw 方程准确是
$$
 H_{tt}-2dH_{t\theta}+(d^2-Qv^2)H_{\theta\theta}
                          +a_1H_t+a_2H_\theta=0,
$$
$$
 a_1={\mu_t-(\mu d)_\theta\over\mu},\qquad
 a_2={-(\mu d)_t+[\mu(d^2-Qv^2)]_\theta\over\mu}.
 \tag{D.22}
$$
S.9 的准确四态恒等式给
$|a_1|_{H^4}+|a_2|_{H^4}<2^{100}J\delta_j^{-3/2}$；
这些式子没有 $Q_t$，也没有把 $C^4$ 形状再作未付高阶微分。
连同 $t=\log r$ 的有界转换与一维角 Sobolev 嵌入，
最终费用小于
$$
                       2^{8192}J^8\delta_j^{-22}A_j^{\rm in}.
 \tag{D.23}
$$
其最大 $\delta$ 幂的账准确为
$15/4+10+7/2+9/2=87/4<22$；
$J$ 幂为 $5/6+5+2<8$。

### 7.2 实际根 collar：两行初值、真实 Jacobian 和密度

使用
[实际联合根图](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
J.16--J.29，以及正根篇 P.5 的**两列及导数**。
根处非zero列为
$c\kappa^{-1/3}(\operatorname{Bi}\pm i\operatorname{Ai})$，
$\kappa=|m|/b$；mean 是 $c(1\pm i\xi/\pi)$。

在负侧 $0\le\xi\le1/64$，原平衡两行
$Y=(s^{1/2}u,s^{-1/2}u_\xi)$、
$s=(1+\kappa^{4/3}+\kappa^2\xi)^{1/2}$ 满足
$$
 \|Y(0)\|_{H^8}\le2^{16}b^{1/3}A_j^{\rm in},
 \qquad
 \sup_\xi\|Y(\xi)\|_{H^8}<2^{2208}b^{1/3}A_j^{\rm in}.
 \tag{D.24}
$$
第一式在 $|m|\ge4$ 上直接由两个初值读取，mean 单独用完整线性列；
第二式是 J.28 的同频参考与 J.29 的完整小 multiplier
在8阶角窗中的 Duhamel，不是单列 Ai 高度界。

$s^{1/2}$ 至多损半个角导，因而 $u,u_\xi$ 的所需角 jet
由 (D.24) 支付；再用
$u_{\xi\xi}=(\xi/b^2)u_{\phi\phi}-Vu$ 支付第二径向导。
J.16--J.18 的真实 Jacobian 及其二 jet 每次径向转换至多
$2^{128}b$、$2^{128}b^2$。
J.24 的完整解析密度比和 $|(\log\alpha_0)_\xi|<8$
给原高度恢复的相同二 jet 界。
若 $q_e=\alpha_{0,e}/(\varepsilon_s/\rho)$，于是足够取
$$
       \|H\|_{C^2_{r,\theta}(\text{负根 collar})}
            <2^{8192}b^3q_e^{-1/2}A_j^{\rm in}
            <2^{9000}J^{3/2}\delta_j^{-10}A_j^{\rm in}.
 \tag{D.25}
$$
最后使用 Z.4 的 $q_e^{-1/2}<2^{512}\delta_j^{-19/8}$
和 $b\le\lambda_j$；
实际最坏幂为 $27/4+19/8=73/8<10$。
没有把大频渐近代替根处 $\kappa^{\pm1/3}$，
也未删除两个 mean 的线性初值。

### 7.3 整个正型分量：完整能量、通量和两端高度

正型区由实际上升 quintic 的两个根界定。
[完整 positive DN](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)
C.2--C.12 给真实全区 form，包括两端互耦和共同常数。
本节不在两 collar 之间添加边界条件。

令 $\ell_I=|I|$，$A=-Q$。原 $x\in[1/4,3/4]$ 子段、实际
$\eta_j$ 及 $1/2<JD^{-3/2}<2$ 给
$$
 2^{-6}\delta_j^{3/2}<\ell_I<\delta_j^{3/2},\quad
 2^{-10}m_j\delta_j<\widetilde\mu<
                   2^{136}m_j\delta_j^{-1},\quad
 A<2^{12}J\delta_j^{-3/2}.
 \tag{D.26}
$$
把真实两端高度记为 $f=(f_-,f_+)$。
其线性 $t$ lift 的参考能量不超过
$2^{160}m_jJ\delta_j^{-5/2}\|f\|_{H^1}^2$。
完整 form 的最小化及 C.8 的实际角解析系数比较，
对至多6个角导作同一个零迹能量修正，给
$$
 E_6^{1/2}\le
       2^{210}\sqrt{m_jJ}\,\delta_j^{-5/4}\|f\|_{H^7}.
 \tag{D.27}
$$
这里 $E_6$ 是 C.5 完整角图后六个角导的参考能量和。
系数角导用宽 $1/8$ 的 $r!\,8^r$、$r\le6$；
$2^{210}$ 同时覆盖乘积计数和真实角图的正逆费用。
不把 radial 圆周的常高度用角 Poincare 删除。

由
$\int_I\widetilde\mu_0^{-1}dt<2^{10}m_j^{-1}\delta_j^{1/2}$
及两端高度，
$$
          \sup_I\|H\|_{H^6}
                <2^{220}\sqrt J\,\delta_j^{-1}\|f\|_{H^7}.
$$
为了求物理径向 jet，使用真正 flux
$\Pi=\widetilde\mu(H_t-dH_\theta)$。
在 C.5 的图中，
$H_t-dH_\theta=u_t-(\chi_t/\chi_\eta)u_\eta$，
而 $\chi_t/\sqrt A$ 有已付界；故 (D.27)
也控制 $\Pi$ 的 $L^2_tH^5$。
这一步不对 $\sqrt A$ 插值图作一个在根上发散的二阶径向求导。

原散度式准确给
$$
             \Pi_t=\partial_\theta(d\Pi-\widetilde\mu Av^2H_\theta).
 \tag{D.28}
$$
先由 $L^2$ 平均选一条截面，再积分 (D.28)：
第一项用 $(\widetilde\mu_{\max}/\ell_I)^{1/2}E_5^{1/2}$，
两个积分项分别用
$(\widetilde\mu_{\max}\ell_I)^{1/2}E_6^{1/2}$
及 $(\int_I\widetilde\mu A)^{1/2}E_6^{1/2}$。
所需实际角乘子在同一宽域内，故可取
$$
 \sup_I\|\Pi\|_{H^4}<2^{400}m_jJ\delta_j^{-5/2}\|f\|_{H^7},
 \qquad
 \sup_I\|H_t\|_{H^3}<2^{512}J\delta_j^{-7/2}\|f\|_{H^7}.
$$
再用 (D.22) 的正区版本，$Q=-A$，
$a_1,a_2$ 的同一 $2^{100}J\delta^{-3/2}$ 门，
得到
$\|H\|_{C^2_{r,\theta}(I)}
 <2^{800}J^2\delta_j^{-5}\|f\|_{H^7}$。

最后，根的完整两波、实际密度和真实端角给
$$
       \|f\|_{H^7}
          <2^{1024}J^{1/6}\delta_j^{-25/8}A_j^{\rm in}.
$$
这是 $b^{1/3}q_e^{-1/2}$ 的准确幂；
mean 单独由 P.5 的 $c$ 读取，仍保两端高度差。
所以整个正分量的费用小于
$2^{4096}J^3\delta_j^{-9}A_j^{\rm in}$。
与 (D.23)、(D.25) 合并，所有实际覆盖和固定邻胞均有 (D.19)。

## 8. 真正物理平端 C²，而非仅角正则性

从 (D.4) 逐层读取
$$
 \|x_{{\rm full},j}\|_{H^8}
       <2^{1608192}J^8\delta_j^{54}\mathcal G .
$$
固定两层邻居的层权比例、每胞根数及实际表示转换均包含在
(D.19) 的固定余量中。于是，对无源深尾，
$$
 \boxed{\quad
 \|H\|_{C^2_{r,\theta}(\text{第 }j\text{ 胞})}
          <2^{1800000}J^{20}\delta_j^{22}\mathcal G .
 \quad}
 \tag{D.29}
$$
$J^{20}\delta_j^{22}\to0$。profile 的原接缝为实际 $C^4$
零延拓，原 physical 高度与 total conormal按准确方程匹配；
在无源、无原子时，$\mu>0$ 的每个有限接缝由 (D.22)
还给第二径向导的相同迹。
因此真实高度、一次导和二次导全部一致，且在平端趋零。
将 $H$ 在平盘内延拓为0，得到真正 $C^2$ 函数。
一般 gauge 则将 $H-\lambda$ 作此零延拓。

回到实际 ambient 极坐标 $a=\rho r$，并再转换平面 Cartesian 导数，
一个明确充分的物理尺度是
$$
 C_{\rm phys}=2^8\sqrt{\rho/\varepsilon_s}\,
                       \max(1,\rho^{-2}) .
$$
于是
$$
 \|h-\sqrt{\rho/\varepsilon_s}\lambda\|_{C^2_{\rm Cartesian}
                    (\text{第 }j\text{ 胞})}
   <C_{\rm phys}\,2^{1800000}J^{20}\delta_j^{22}\mathcal G .
 \tag{D.30}
$$
原 $\rho,\varepsilon_s$ 从未设为1；ambient 高度变化与 raw
deflection 的相反号不影响 norm，但重建时仍沿原约定。
本结论不给未经此实际尺度收费的统一曲率/reach 小量。

## 9. 完整已证源范围及下一条必要费用

本篇已经给所有满足 (D.3) 的原位完整源以 (D.4)。
其系数和两个 $\Gamma^*$、$\nu$、独立外返列均按原 map保留。
若实际物理源径向紧支，且在其有限支持区的原 source 窗足以给
经典二 jet，那么剩余深尾确实齐次，(D.29)--(D.30)
给整个平端的 $C^2$ 接合。有限有源区的普通 regularity
使用其实际 source jet，不由“根源紧支”自动授予。

若源在无限多个深胞内非零，则只控制根 source 的 (D.3)
仍不够。可以取同一胞内的零端迹 particular，使根荷很小而
二阶导很大。因此要把 (D.30) 扩到这些原源，必须另逐片付：

* root 的完整 Piola ordinary/weak 源在真实 $(\xi,\phi)$
  域中的窗口，及 total/bare 法向的正确区别；
* strict 的 S.33--S.36 完整源，包括弱径向源在高度 mean
  中的 $-\langle\nu F_d^t\rangle$；
* positive 的 C.25--C.33 完整双端 contact/零迹 particular，
  其胞内物理二 jet，以及有原子时的单侧迹和 BV 解类。

这些 specific particular 费用还未包含在 (D.29) 中。
本篇没有把有限 $H^{1024}$ 变成原 $\ell^1_{224}$ 指数标签，
也没有由固定背景的线性 $C^2$ 延拓关闭 nonlinear 方程、
moving/full-$\delta$ 帽 Hessian 或真实 $\nu$/joint Schur。
它完成的是原全混频逆到强层衰减、以及实际齐次深尾物理平端
二阶延拓的完整接线，无新增数学数值计算。
