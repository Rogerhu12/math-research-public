# W / gamma 非零：由原三次迹直接得到全图首一 f² 与完整十行二列

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

这是替代尚未执行的 3ffb / QQ(e,k)[s] 头 Euclid 提案的新原输入。旧提案保持未执行冻结，不标作失败。
新源 2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py，
16808 字节，SHA256 bd68e5e5e66f31e9c3e2ad0b66468c021fc7d852d44462d3a937966200ab961c；
首次 180 秒 / 4 GiB，仅一个固定 C9 定义源依赖。新源尚未执行。

## 1. 同一个完整原斜率图

当前 W 已付 $t$ 与 $\eta=f-u$。取
$$
s=t/\eta,\quad \delta=1-Q,\quad m=u-\ell,\quad
\widehat U=u-\ell Q,\quad M=\ell(2u-\ell Q)-u^2,
$$
$$
\gamma=4\delta-\widehat U s.
$$
只处理实际 $s\gamma\ne0$；原 $\alpha=\eta\gamma$。整个 $\alpha=0$ 的四重二次域另线保留，不因本输入而被删除。

正确原 $R/\eta$ 给
$$
V=\frac{\beta f+c_*}{\gamma},\qquad
\beta=4\delta-2um\,s-\frac M4s^2,\qquad
c_*=-s\left(Mu+\frac m2T_0\right)+\frac{Mu}4s^2,
$$
$$
W_1=(T_0+4uf)/2,\quad
x=(\widehat U V-mW_1)/M,\quad
y=(\ell W_1-uV)/M,\quad t=(f-u)s.
\tag{1}
$$
所有 $x,y,t,\lambda,T$ 对 $f$ 一次。完整真 dual Gram 核同点 $E_0,N_0,P_0,P_1$、$E_1=EW$，留下
$$
Q_0=EW,\quad Q_1=EBo,\quad Q_2=N_1
$$
三个 $f$ 二次以及原 $Q_3=NS,Q_4=PS$ 两个 $f$ 三次。

## 2. 全图显式头 Bézout 的原三次来源

使用已发表的 native 六规则。四个原二次
$$
F_0=E_1,\quad F_1=EBe,\quad F_2=EBo,\quad F_3=N_1
$$
通过已付权变换给首项 $x^2,xy,xt,t^2$；两个原三次 overlap 给首项 $y^3,y^2t$，余项都在
$$
1,x,y,t,y^2,yt
$$
中。六条规则的原组合迹已保留；两条三次规则的原 $F_i$ 乘子至多一次。

这组规则原来标记的 $(k+2)J19C9$ 现已经由三个整支定理支付：

- R150-appendix-unit211-equal-weights-complete-original-exclusion.md；
- R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md；
- R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md。

本源再次对真正选定的 $\delta_2,\operatorname{num}(\delta_3),\operatorname{den}(\delta_3)$ 只用这些已付原权因子剥回，而不是把旧 chart 标签当成单位证明。

定义原齐次线性式
$$
f_h=\frac{ux+\widehat U y}{2u}.
$$
按同一六规则只作一次**新的** $f_h^3$ 还原，得到
$$
f_h^3-r=\sum_{i=0}^3 a_iF_i,\qquad
\deg r\le2,\quad \deg_{x,y,t}a_i\le1.
\tag{2}
$$
没有 NS/PS 的三次来源项；源码核两个对应 trace 系数为零。取齐次三次部分，设 $a_i^{[1]}$ 为一次部分，便有完整原身份
$$
f_h^3=\sum_{i=0}^3a_i^{[1]}F_i^{[2]}.
\tag{3}
$$
这是带原乘子的真实多项式身份；不要求原六生成元自由。

令 $x_f,y_f$ 是 (1) 的 $f$ 系数。准确有
$$
ux_f+\widehat U y_f=2u,\qquad t_f=s.
$$
故在方向 $(x_f,y_f,s)$ 上 $f_h=1$。设三个当前二次的 $f^2$ 头为 $h_0,h_1,h_2$。由同一个原均值变换，
$$
F_0^{[2]}=h_0,\quad
F_1^{[2]}=(h_0-mh_1)/\ell,\quad
F_2^{[2]}=h_1,\quad F_3^{[2]}=h_2.
$$
把 (3) 代入这一方向得到明确
$$
\boxed{c_0h_0+c_1h_1+c_2h_2=1,}
\tag{4}
$$
$$
c_0=a_0^{[1]}+a_1^{[1]}/\ell,\quad
c_1=a_2^{[1]}-m a_1^{[1]}/\ell,\quad
c_2=a_3^{[1]},
$$
各 $a_i^{[1]}$ 都在该方向求值。

(4) 的分母只有原已付权因子与 $\gamma$，没有新的未知权覆盖 $C$。新源会按单项式显式从旧 8 变量 context 嵌入当前 4 变量 context，并完整返三个当前原头的乘回；不会混用相同变量含义但不同 context 的对象。

因此在整个当前 $\gamma\ne0$ 图上，准确的原组合
$$
\boxed{q_f=c_0Q_0+c_1Q_1+c_2Q_2=f^2+q_1f+q_0}
\tag{5}
$$
是首一二次。此纸面构造不依赖未知的函数域主元，也没有把尚未实算的系数 profile 声称为已执行结果。

## 3. 完整原 I6 的十行二列与后继原标量

用 (5) 对全部五个 $Q_i$ 首一除法：
$$
Q_i=A_iq_f+r_i,\qquad \deg r_i\le1.
$$
再求 $fr_i=B_iq_f+r_i'$。每个 $r_i,r_i'$ 都保存五个原行的完整多项式乘子，所有五源组合与首一商积都实际返回。十个余式的两列对应真实非零值列 $(1,f)^T$。

$EW,EBo$ 恢复 $EB,EC$ 只除已付 $\ell$；$E_1=EW$、$E_0,N_0,P_1$ 都在同原点精确恢复，所以这保留完整原 I6。没有把一般值列自由化或以交换矩阵项为零替代原点关系。

首一环境本身自由秩 2；物理原图仍带 $\eta=f-u$ 等局部化和其余个别值条件。本输入不据此无条件声称原物理商对整个参数环有限自由。

后续只取两个真正非零常数列组合。约去的仅是两个实际行乘子的公因子，随后返两列和五原迹；并不除未知原方程因子，公因子零面保留。本次成功与否均不预宣整个 W 排空。

## 4. 冻结依赖与执行边界

唯一依赖：
2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py，
完整 SHA256 10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1。

只执行其截在 matrices=[];errors=[] 之前的 14656 字节必要定义前缀，
SHA256 88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8。
它包括六条原规则及 reduce_six 定义；不执行旧十八乘法列、旧 NSPS/comm 参数余子式或任何旧大门。

两种计时 API 都被钳到新源最初的 180 秒绝对截止；前缀和顶层地址空间硬界同为 4 GiB。
只输出源、参数定义、次数/SHA 和小回执，不写可重算系数或矩阵缓存。
