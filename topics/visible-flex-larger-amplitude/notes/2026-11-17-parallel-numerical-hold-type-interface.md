# 同g唯一曲率变号接口的真实全模态到达

**有限真实接口，不是DN或闭合结果。** 在固定HoldProfile的rise中，κ=−5/2+4S(u)，S=10u³−15u⁴+6u⁵。因S′=30u²(1−u)²>0于(0,1)，方程S(u)=5/8有唯一解，指定

\[
s_*=1017/1000+u/50.
\]

选择器以80次精确有理二分记录该根的区间，再取相应binary64时间 **1.0283496328972757**。这是一条由标量方程指定的变化型接口，不是试探终点扫描。report保留有理区间及浮点时间与区间的距离上界（约3.87e−17）。

只从原6529成功IVP的1.02末态新积分至此，**不从先前失败raw截取父**。原M320/N4096、962个ODE、rtol1e−13、atol1e−16、first/max step=1/64000保持。启动前重新计算RHS和JVP二阶导数，与保存的0/1/2jet逐位差[0,0,0]。

本次536个新节点、6421次RHS、37.78秒，真实达到指定端点，failure=null。保原1601节点后去重追加535节点，raw合计2136节点，保存每节点全部962个state/rhs/d2分量。明确`ivp_reached_end=true`、`bvp_accepted=false`。

## 实际端点

|量|实际读数|
|---|---:|
|a|1.1810986109937334|
|a′|.4120828321070139|
|a″浮点评估|1.1329647820106724e−14|
|κ浮点评估|−1.2434497875801753e−14|
|Qmin|.03844896256794784|
|Wmin|.00035467592782154506|
|Hmin|.00034751142434276145|
|k=a′/a|.3488979059591836|
|min sqrt(W/Q³)−abs(k)|.11726230939581384|
|8192角实际RHS相对Gram|6.941694066231463e−7|

Q/W/H的4096和8192角读数在显示精度下相同。数学标量接口上a″=κ=0；表中的非零小量来自浮点求值。a′>0使此接口仍可换到物理半径r=a局部坐标；它没有支付未来椭圆侧的非线性DN或向内转向。

本项是实际端点及保存的有限IVP数据，不把端点Gram代替整段共同quintic读出，不冒充高模/角网格/径向收敛、闭合、reach或全t结论。以后采用该接口还须读取完整实际trace，不能用轴对称参考曲线替代。

## 复现与身份

S为本题scripts目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_type_interface.py" --input parallel-negative-hold-ivp.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --resume-source "$S/parallel_20261117_hold_resume_ivp.py" --out parallel-negative-hold-type-interface.json
```

SHA256：

- 原输入：`6529073f7ad1c5f041e5f7be921a2dab6f509768622153a770556d0460a5a6be`。
- 唯一接口选择器：`ffaf122f003e18b44f6da93743ba405d0e3e82bea4b1935a20316d30662b8e69`。
- 实际续算源：`e773a7066045fb164894370b9f53e02bb2140b47e4cc23d4e053cca55f2b8c15`。
- 固定HoldProfile源：`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
- 实际raw：`a425e38ed4caeebf4d1f96629721c2ba1f54d72eef863ac278e7fb64f0327ba8`。
- 实际report：`ff534efb1abef1b930ee0b02c05f76ef09c07aeed9e764ed334969bab6517f22`。

raw保留原续算源身份；report另记`interface_selector_sha256`与`mathematical_interface`。新段统计以`continuation`/`true_ivp_continuations`为准，全部raw留scratch。
