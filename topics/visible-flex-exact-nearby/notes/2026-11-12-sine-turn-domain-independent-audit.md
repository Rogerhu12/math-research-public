# 准确 sine 时间像、负径向反射与消根域的独立核查

2026-11-12，independent_audit。已通读以下源码及 real_anchor/Fourier
费用的调用，未为此重跑已完成的区间作业。

- `fourfold_phase_sine_time_geometry.py`：
  `c369f202fed14a6951b44cfaf3e3890841814c15040f0d15773d2bc61b189efa`。
- `fourfold_phase_full_angle_sine_domain.py`：
  `b7b05da28d63c186b4cfbefb09de1f96c6e82f98ed9146f7358ac31ad5bddd3a`。
- 被复用的 `fourfold_phase_full_angle_time_domain.py`：
  `d681614326efacb0c256037d2c7e995eb895d8f77ce4281720f44c76a896548e`。

上述文件均位于本课题 scripts/。本核查只涉及域接口；数值通过值以
各自绑定源码 SHA 的真实报告为准。

## 1. sine 像保留同一实际中心

由 sin(tau+z)-sin(tau)=sin(tau)(cos(z)-1)+cos(tau)sin(z)，以及
|cos(z)-1|<=cosh|z|-1、|sin(z)|<=sinh|z|，源码的

\[
|t\sin(\tau_c+hu)-t\sin\tau_c|
\le |t|\{ |\sin\tau_c|(\cosh H-1)
                    +|\cos\tau_c|\sinh H\},\qquad H=|h|R
\]

成立。中心和径向像使用同一个真实根 t，没有把 t 的区间中点当作
准确根。转折处一阶速度为零的收益被保留。其后实际 germ 的完整
多项式延拓只服务该 germ 的域；完整实际时间段仍由所有相交 spans 的
有限并覆盖，未授予跨 knots 的径向解析性。

## 2. 反射和 time 坐标没有丢符号

显式对称性给 F(-r)=S F(r)，S=diag(1,1,-1)，而 Fr(-r)=-S Fr(r)。
故 D 偶、M 奇，W 及同步目标 K 偶。源码只反射引用 R59 的实际 anchor，
没有把原来的负径向系数和 jet 改名为正径向系数。

proxy 同时取 tau0→-tau0、h→-h，于是它求出的
u_anchor=(asin(r_anchor/t)-tau0_proxy)/h_proxy，正是原时间坐标中的
anchor。当前物理 sine 支是 tau∈[-pi/2,pi/2]；asin 在此取相同支。
这是该 anchor 公式的范围条件，不能无条件用于其他 sine 周期。

D(u)-D(u_anchor) 的常数项准确抵消。保留 time 系数的差、R 处的尾
和 anchor 处的尾全部计费，再从 R59 的完整角带模下界相减。这里只需
模下界，不必把一个复域模下界误当成实部下界。

## 3. 真实消根 Q 及两端波因子

转折模型分别使用 eta=pi/2-side*tau 和已付的真实
Q=-K/sin^2(eta)。它先在更大时间盘上认证 Q，再对实际工作盘的
完整 time 尾付费，并要求 Re Q>0。代码没有在跨转折的复盘上要求
Re(-K)>0。

在真实内侧，两端都有 r_tau=t sin(eta)，而波因子为
sin(eta)sqrt(Q)。后者给穿过端点的解析延拓；Q 的平方根由正实部
选定。D/M/W 的粗域计算不除 D、不取曲率平方根，故它们本身的解析
预算不依赖先付普通负曲率域。

源中最终 f、f_theta、f_thetatheta 的模预算使用 M+|wave|W，因而
对两种 branch sign 均有效。实际分支与方向仍由 native field 对象
记录，不因取模预算而被删除。未发现此轮新增接口的实质错误；其结论
仍是所列时间段的完整域，不是 flow 残差或返回共轭证书。
