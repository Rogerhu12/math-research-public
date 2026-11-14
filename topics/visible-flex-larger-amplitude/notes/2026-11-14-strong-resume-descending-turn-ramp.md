# 主下降转弯 ramp fraction 的可执行接口

**可信度：C² 接合公式已证明；接口逐点/完整数据相同性为数值证据。没有新非线性曲面解。**

原 `alternative-neck-flatturn.turn` 将 flat-top ramp fraction 固定为 `0.08`。新增 `descending_turn_ramp` 只作用于第一个从正径向速度转为负径向速度的真实 turn，保留其角端点和峰值角速度 $K$。其余同步段、回环和有限 terminal bridge 不改公式。默认不提供新参数或显式取 `0.08` 时，所有原 A 的 segment 字段、系数、phase、长度和累计背景位置均与旧构造逐字相同。

## 数学接口

取 $0<\varepsilon<1/2$。原对称 ramp 为
$$w_\varepsilon(u)=3z(u)^2-2z(u)^3,\qquad
z(u)=\min\{u,1-u,\varepsilon\}/\varepsilon,$$
其中在端点之外只按原分段定义取值。令
$$I_\varepsilon(u)=\int_0^u w_\varepsilon(v)\,dv,\qquad
L=\frac{|\phi_1-\phi_0|}{K(1-\varepsilon)},\qquad
\phi(u)=\phi_0+\frac{\phi_1-\phi_0}{1-\varepsilon}I_\varepsilon(u).$$
由左右 ramp 各积分为 $\varepsilon/2$、中间平台长度为 $1-2\varepsilon$，有 $I_\varepsilon(1)=1-\varepsilon$。因此两端角恰为原 $\phi_0,\phi_1$，并且
$$\frac{d\phi}{ds}=\operatorname{sgn}(\phi_1-\phi_0)K w_\varepsilon(u).$$
用原转弯模型的真正积分定义 $a_s=\sin\phi$、$z_s=\cos\phi$。两端 $w=0$，故
$$a_{ss}=\cos\phi\,\phi_s=0,\qquad z_{ss}=-\sin\phi\,\phi_s=0.$$
这同时匹配相邻 coast 的完整一、二阶 jet。各位置用积分累计，并按原 coast 公式回接指定半径，得到位置连续。只要原有限 piece 的正长度及 $|a_s|<1$ 条件保持，完整轴对称背景 $(a(s)\cos\theta,a(s)\sin\theta,z(s))$ 的全部零、一、二阶接合成立。这里不能仅凭回接半径就断言接合，角端点与上述二阶条件同样必要。数值实现沿用原 Gauss 积分计算这些积分，没有换积分规则。

## 实际检查

原 A 的完整 profile 作为输入；没有加载 Flow IVP、BVP Jacobian 或尾 worker。对 $\varepsilon=0.08,0.07,0.09,0.12$，实际构造了所有 pieces，检查每一个内部、prefix-to-bridge、bridge 内部接合的 $a,a_s,a_{ss}$，以及轴对称背景完整 XYZ 的 0/1/2 jets。最大跳量为 `5.551115123125783e-16`。完整入口 scalar jet、prefix-to-bridge scalar jet 和物理 cut scalar jet 保持原值；整个有限 bridge 的完整 segment 数据及整个 tagged physical tail port 逐字相同。

| $\varepsilon$ | Prefix 长度 | 背景 Prefix 高度 |
|---|---:|---:|
| .08 | 3.14101574976516 | 1.96188568384143 |
| .07 | 3.13719580949123 | 1.96032101684016 |
| .09 | 3.14491756235731 | 1.96349477968951 |
| .12 | 3.15714148808505 | 1.96860695418533 |

非默认值改变 prefix scalar profile，因此全局 $g$ 是**新设计**。只能说原 tail 的 $g$/cut 和相对 finite-bridge 几何不变；新 prefix 累计高度本来允许变化，接尾时按新高度平移。这里没有检查非圆实际曲面完整 XYZ 的接合，也没有计算这个新设计的真实 14 方向响应、Newton 解、闭合族或 reach。

源为 `computations/strong_20261114_descending_turn_ramp.py` 与 `strong_20261114_descending_turn_ramp_check.py`。小接口报告和复算 argv 在同名 `-r1/` 目录。未来实际 BVP 需要把此 provider hook 同时装入真实构造、保存态读取和响应路径；该装配尚未执行，不能称为完整新增 BVP 控制已可用。当前主线仍是原 13 方向半步的实际求解。
