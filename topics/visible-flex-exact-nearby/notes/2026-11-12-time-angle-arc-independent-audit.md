# R61 时间—初始角双变量局部证书独立核查

核查日期：2026-11-12。核查者：independent_audit。
已完整逐式阅读两份源码，并核对以下两份报告与当前来源 hash；没有重跑完整轨道，
也没有将局部 arc 结论升级为全圆、全支流、完整返回或最终 KAM 证书。

## 1. 冻结来源与范围

- [fourfold_time_angle_jets.py](../scripts/fourfold_time_angle_jets.py)，
  SHA256 f452fe515af7bea2eeee3c715c158817a317671517ec719ccf9b15725af70cbd；
- [fourfold_phase_time_angle_residual.py](../scripts/fourfold_phase_time_angle_residual.py)，
  SHA256 bbf488eea30479b98a97b82a564bb7cbd83f63b5e6650fd568ef68b0470abd8e；
- [第二点报告](2026-11-12-R61-step2-time-angle-arc-pilot.json)，
  SHA256 cb0b68d59288ea42158e13e031fe799a21dd7f4aa5f8e3f3fd175763cb8c9e4e；
- [第三点报告](2026-11-12-R61-step3-time-angle-arc-pilot.json)，
  SHA256 1ef5900931f21683d2317927e6c7b2748c186c3e39d488375f4bec09c05daa05。

两报告分别对应第二点 reference segment 653 和第三点 segment 419，
各自在该段的准确归一子区间 \([31/64,33/64]\) 上。
初始标签为

\[
x=\frac12+\frac{i}{512}+\frac{v}{4096},
\qquad -1\le v\le1,\quad v\text{ 为实数}.
\]

实际物理角状态是 \(Y=x/4+U\)，不是 \(x+U\)。
保留次数为 time 16、angle 23；外双圆盘半径为
\((R_t,R_x)=(8,4)\)。

第二点对象/根 SHA256 分别为
aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1 和
c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb。
第三点分别为
e6ff2d46ed2d321c1b287e6c9d8e44ead7b9a70523350d145d703b4edd6def0f 和
afdc964a11682f9c54ceb1e6a165950f007ea26ab917f8dbde8b38c9fe78629f。
源码检查这些身份与 reference manifest 的对应关系，不能互换两点。

## 2. 有限代数确实是矩形商环

源码的系数是 \(\sum_{i<m,j<n}a_{ij}u^iv^j\)。
将 \(u^iv^j\) 放在单变量多项式次数 \(i+(2m-1)j\)：
相乘时两个保留 time 次数之和至多 \(2m-2\)，严格小于 stride，
故被丢弃的高 time 次数不会进位污染下一 angle 行。
每次乘法后显式保留矩形 \(i<m,j<n\)。

仅 time 的因子采用逐角行 native series 相乘，与同一矩形商环一致。
inverse、exp、sqrt、log 的 angle 递推是在
\(\mathbb C[u]/(u^m)\) 上实施准确形式幂级数运算；
例如 \(j(\exp f)_j=\sum_{k=1}^j kf_k(\exp f)_{j-k}\)。
源码还用准确有理系数和特意构造的 carry trap 核对代数。
这些代数检查自身不提供解析余项；余项另由第 4 节支付。

## 3. 无限原函数及物理角的接线

只在 \(v=0\) 调用冻结 native time 原函数，并用已支付外 time 圆盘误差
\(\varepsilon_X/R_t^i\) 加到每一个 time 系数。

随后用旋转柱坐标分量的准确恒等式

\[
X_\theta=a'T+aT_r-J_{\rm rot}X,\qquad
J_{\rm rot}(X)=(-X_1,X_0,0),
\]

乘真实 \(Y_v\) 并逐 angle 次数递推 \(X(u,v)\)。
这一步用的是实际几何恒等式，未把截断 Fourier 原函数的角导数
冒充无限原函数角导数。递推中初值误差也跟随同一线性 ODE 的系数运算传播。

phase 采用 \(\exp(\pm4iY)\)，对应物理角 \(Y\)；
参考中的 \(x/4\) 和 \(Y_v\) 的 \(h_x/4\) 都显式加入。
参考的时间导数除准确物理 time 半宽 \(h\)，没有额外乘 4。

真实场与其物理角导数由同一几何分母 \(D\) 计算。
代码另核 \(\partial_v f(\tau,Y)=f_\theta(\tau,Y)Y_v\) 的第一 angle 行，
两份实际报告均通过。此恒等式是有用的交叉检查，不能单独替代外圆盘误差证明。

## 4. 完整参考像和两类 Cauchy 尾

有限 Fourier 参考对复初始角本来是整函数。
其截断 angle Taylor 多项式之外的真实变化由完整正负 Fourier 模对估计。
正负共轭配对给 \(2\cosh(k\,\operatorname{Im}x_0)\)；
再乘 \(\exp(kh_xR_x)-1\)，并对 time 系数按 \(R_t^i\) 求和。
因此 outer_domain 包住的是完整有限 Fourier 参考的外双圆盘像，
不是仅包住已保留的 angle Taylor 多项式。

外域门同时支付原函数无限尾、径向实际 common span、
\(\operatorname{Re}(-K)>0\)、真实 \(D\ne0\) 和复角带宽。
若实际场在外双圆盘模不超过 \(M\)，遗漏矩形的总系数和由

\[
M\,\frac{R_t^{-m}+R_x^{-n}}
        {(1-R_t^{-1})(1-R_x^{-1})}
\]

控制；重叠角落至多被安全重复计算。

参考在 time 上只有 7 次，故其导数没有未付 time 尾。
参考的 angle 尾另以完整有限 Fourier 导数在
\(|u|\le1,\ |v|\le R_x\) 上的模界支付
\(M_{\rm ref}R_x^{-n}/(1-R_x^{-1})\)。
不能用上式中的真实场尾替代这一独立参考尾，源码没有这样做。

\(L\) 的值尾也独立计入。由 \(\operatorname{Re}L\) 的上下界得到
\(q_{\min}\le|\exp L|\le q_{\max}\)，对复参考弧同样有效。
局部 R60 的源项和二阶场界采用同一 state tube，
且只在另外假设左端真实状态与参考状态相等时给出零初始误差的局部结论。

## 5. 两个实际局部结果

| 实际对象及段 | \(\|Y_\tau-f\|\) 严格上界 | \(\|L_\tau-f_\theta\|\) 严格上界 |
|---|---:|---:|
| 第二点，653 | \(4.593373\cdot10^{-7}\) | \(5.729013\cdot10^{-4}\) |
| 第三点，419 | \(7.420387\cdot10^{-10}\) | \(1.622920\cdot10^{-7}\) |

第二点的两项双 Cauchy 加参考尾分别小于
\(6.281787\cdot10^{-15}\)、\(1.950875\cdot10^{-13}\)；
第三点分别小于
\(5.914534\cdot10^{-15}\)、\(1.537876\cdot10^{-13}\)。

核查结论：上述源码的矩形代数、无限原函数接线、物理 4 因子、
完整外域像和两类尾费用在声明范围内成立，未发现实质数学缺口。
这里尚无整条边界圆、所有 time 子段、两端转折 collar、累积初始误差、
完整真实返回或参数变分证书。

