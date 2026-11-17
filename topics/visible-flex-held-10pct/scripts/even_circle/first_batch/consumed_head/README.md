# 四重圆弧核心的消费窗口短子午线

此包给两个实际线性根和可重算的显式子午线公式，不给非线性等距前缀或闭曲面。父会话已用 case1 启动真实 n4 边值问题。两个设计都用原 m4 真实尾启动端口，cut 为 r=.3、w=.08、w_r=−7w/r；其频率为 4,8,…,32，首列 D4=31.30504136633579。

## 配置接口

```python
import consumed_short_profile as profile
profile.configure(HEAD_SOURCE_PATH, SHORT_BRIDGE_SOURCE_PATH)
f = profile.ConsumedShortLoop(port['cut'], **parameters)
a, a_s, a_ss = f.profile(s)
```

`HEAD_SOURCE_PATH` 是已发布 `scripts/plateau/consumed_window_profile.py`；第二个参数是 immutable source 中 `topics/visible-flex-larger-amplitude/computations/root_short_bridge.py`。函数及实际消费源 SHA 见 manifest。`f.parameters` 不包括 cut，调用者必须将同一个真实端口的 cut 传入。`end`、`breaks`、`Tu`、`prefix_end` 和 `profile` 可直接供 `window_prefix` 式 Flow 包装使用。

`case1-profile.json` 和 `case4-profile.json` 是两个冻结设计输入。`stop_acceleration` 可作为非线性设计控制；一旦固定完整 g 精化，它应固定。整个 head 不再保护旧前缀上的 H，新的 H 位于单独的中央直柱。

使用 warp=0 和解析核心 lift。归一化线性 F/a 在中间可低至约 −3.55；将它直接乘 15q 作为高 q 的角 warp 会破坏角图可逆性。

## 再生

```sh
python screen_consumed_short.py --port MODE4_PORT8 --head-source HEAD_SOURCE --short-source SHORT_SOURCE --out SCRATCH_SCREEN
python audit_consumed_roots.py --port MODE4_PORT8 --head-source HEAD_SOURCE --short-source SHORT_SOURCE --root SCRATCH_SCREEN/case1-root1 SCRATCH_SCREEN/case4-root2
```

筛选只有六组明确的早段设计和六个 stop 控制值，没有巨量随机扫参。线性 ODE 从端口逐段反向积分，频率直接读 `port['modes']`，没有复用硬编码的 m3。首列根以外七列的横截性都做了实际计算，但这只是有限线性诊断，不是全模可逆性证明。

`linear_root_summary.json` 保留冻结参数与必要标量。完整运行期八列、chart、采样点和其他可重算数组只留 scratch，不在本包中。

## 结论及局限

case1 的背景高度约 1.04452，加入上下平移 ±.35 的中央柱后，背景采样球半径约 1.58224；case4 相应约 1.00291 和 1.54786。名义尾部再上升 .025 的半径估计均更小。这里直接计算 sqrt(a(s)^2+(z(s)+.35)^2)，没有用包围盒对角。

背景曲率公式上界分别为 6.875、约 7.23747；它对应解析原函数定义的理想子午线，继承 ShortBridge 的 64 点求积实现尚未新增区间误差证书。球半径也仍是采样。真实非圆前缀、实际尾部容量、全相位度量及无限尾、接缝、reach 均需另做。

头部的圆弧特征窗口消耗有独立有理证书，见 `head_certificate.md`。它只排除“已知圆弧唯一性菱形还覆盖首正 K 带”的旧障碍，不保证非线性边值可解。
