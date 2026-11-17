# 一个负曲率 hold 新设计及真实 M320 IVP 到1.02

**数值证据。** 从真实已接受d644的s=.995切口和原core出发，零补至M320/N4096，保全部962个ODE，只运行下述一个新g。原rtol1e−13/atol1e−16、max_step=first_step=1/64000不变。DOP853真实到达 **s=1.02**：1601节点、19201次RHS、46.33秒，failure=null。它不是旧pulse的精化，不是完整BVP接受，也尚未与旧前缀C²接合。

## 固定标量定义与预算

切口a/a′/a″沿原Profile，κ₀=2.15275972133223，α₀=asin(a′)=.3553062405211762。κ依次为：用五次smoothstep在.002内从κ₀降至−2.5；保持.02；在.02内升至+1.5；保持正平台P；末.02降至0。每段ramp为κ=κ左+(κ右−κ左)S(u)，S=10u³−15u⁴+6u⁵。定义α=α₀−∫κ，a=a_cut+∫sinα，参考高度增量=∫cosα。P由最终α=−π/2唯一决定。

本次P=1.314299871729827>0，参考末s=2.371299871729827、R=.5647341753868044、高度增量.9745792944436601、弧长L=1.376299871729827。所有前段负曲率绝对值不超过2.5，故α≤α₀+2.5(.002+.02+.02)=.4603062405211762<π/2；恢复正曲率后α单调降到−π/2。起始短段α仍正，半径唯一最大值在正平台的α=0点：1.2414008202004037；末半径正，参考不穿轴。切口三标量jet实际差[0,0,0]。

以真实cut的φ高度均值加参考高度所得H_ref=1.9478402241037838；对原core材料角Θ的8192个角，真实cut到(RcosΘ,RsinΘ,H_ref)的三维chord最大1.297124519728105，较L少.079175352001722。这只是必要长度门的采样。轴对称参考盒给D_ref≤4.61959198849；实际core gap=.960001022540。**H_ref和D_ref均不是未来非轴闭面的实际高度或直径，不据此声称幅度/reach完成。** 位置积分的数学定义为精确积分，Gauss32只是数值求值。

## 真实终态

N4096末态Hmin=.00046443755；独立N8192为.00045911217659。k=a′/a=.340856160779，对该真实曲线的采样允许值min sqrt(W/Q³)=.465730031441，余.124873870662。末节点RHS的实际Gram为5.55094256658e−7；它不能代替全段quintic读出、C²接合或全域误差结论。

真实1601节点的states、rhs和同源JVP d2已保存，未改变任何被拒尝试，也没有扫描幅度/步长。数据明确ivp_reached_end=true、bvp_accepted=false、old_prefix_C2_join_completed=false。下一几何构造需实际共享首端二jet，不能直接把M320重算的首导数冒作原M112值。

## 正确接口与复现

导入本源的 `HoldProfile(geometry, origin, cut=.995, quadrature=32)`；geometry/origin取d644，完整新标量描述在 `hold_scalar_profile`。**旧h.profile_from不认识这个g，不能用原inward或pulse替代。** 字段中source与hold_profile身份均绑定本源。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_negative_hold_profile_ivp.py" --parent parallel-continue0995-m112.json.gz --out parallel-negative-hold-ivp.json
```

S为本题scripts目录，raw仅scratch。SHA256：

- 左父：`d6441e642b0bb0903915d42e0d4dd9fd564a2e0378e32070110fe6cc7922403f`。
- 本源：`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
- `parallel-negative-hold-ivp.budget.json`：`7c5228408d0ad5bf1e3083237bdb87dbe9963c17488a59b21341f3e727f2931f`。
- `parallel-negative-hold-ivp.json.gz`：`6529073f7ad1c5f041e5f7be921a2dab6f509768622153a770556d0460a5a6be`。
- 实际report：`f496763fc22588774820adb6e3955550a155a4faa08d53654ba4025f986bde3d`。
