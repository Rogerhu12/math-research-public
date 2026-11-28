# 全12876列log-radius设计：真实FD门失败与同算子缩步核实

新g设计支以完整G10零alpha、zero6位置场起算。原streamed设计入口在任何normal/非线性尝试前，对4291840行、12789XYZ+87alpha=12876列做实际完整联合导数门，因其仅试1e−6/1e−7/1e−8的中心差分未过2e−5而自然exit1。外部34.065994188秒，child RSS449340KiB。初态已经保存，R14²=9.491143500485906、alpha全零；设计尝试/接受均0。原失败与代码保留，不称接受。

独立完整审计消费者重新建立完全相同实际场/目标/行列/算子，重复原seed=2026112819的欧氏归一裸系数探针，然后实测更小步长和Sobolev缩放探针。没有修改J/JT公式、任何目标行、来源或门槛。

| 实际裸方向epsilon | 相对L2差分误差 |
|---|---:|
| 1e-06 | 0.01731346001503659 |
| 1e-07 | 0.0035842858303447404 |
| 1e-08 | 0.00015206826862960372 |
| 1e-09 | 1.714567965457627e-08 |
| 1e-10 | 1.4836198108003132e-07 |
| 1e-11 | 1.7603135856778825e-06 |

同裸方向J像范数589.016296351，adjoint相对差9.39593209191e−15。eps=1e−9取得1.71456796546e−8，eps继续过小则舍入误差增加；因此原三步扫描没有解析到此实际方向的有效差分尺度，不能把那个失败直接当联合导数公式错误或忽略它。

同完整物理H2逆三角缩放的联合方向J像范数2.40375595740，eps=1e−7相对FD误差3.84068049062e−8，adjoint8.43580943967e−15。完整87alpha-only方向的eps=1e−5误差3.65820803358e−11、adjoint2.08166817117e−17；这个独立探针包括实际所有active q2面积行与完整metric quartic增益导数。

审计自然exit0，48.258479010秒，RSS482756KiB；没有优化尝试或接受。它核对本真实大场微分，不声称全normal已付、未来试步可接受、连续等距或reach。

新消费者 `2ecf-polar-log-radius-streamed-fd-design-solve.py` 保全部已审计算子与原数值接受规则，唯一区别是原裸方向FD扫描扩展到1e−9和1e−10，并在gate前保存/输出完整derivative check。adjoint门1e−10、FD门2e−5原样保留，模型显式绑定该新检查协议及源码SHA。新设计epoch从同一全零alpha和同一zero6位置场重新支付baseline、计数0起算；旧exit1不抹除。全normal与实际设计试步已在该新入口启动，结果另以自然退出登记。

复现命令（W/S定义和G10 prepared见G10完整基线note）：

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-full-derivative-audit" -- \
  python3 -u "$W/2ecf-polar-log-radius-full-derivative-audit.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --state "$W/polar-design-G10s-step01-initial.json" --output "$W/polar-design-G10s-full-derivative-audit.json"
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fd-step01" -- \
  python3 -u "$W/2ecf-polar-log-radius-streamed-fd-design-solve.py" --scripts "$S" \
  --prepare-entry "$W/2ecf-polar-c2-g10-split-prepare.py" --prepared "$W/polar-c2-G10s-prepared.json" \
  --warm-state "$W/polar-G10s-baseline-zero06-initial.json" --prefix "$W/polar-design-G10s-fd-step01" --steps 1
```

| 文件 | SHA256 |
|---|---|
| `2ecf-polar-log-radius-streamed-design-solve.py` | `2a62893d8b04c2c3b22859c8c9ffd94f8ee7d90996d077642c19f091a3c33303` |
| `polar-design-G10s-step01-exit.json` | `0ef2802db16979dd76ec6b45906d37924ab8d1bdec4dd88fc818e0f832020906` |
| `polar-design-G10s-step01-initial.json` | `d513796d88066454919ecb3af96236f4dfc3235e086104eeb3f9120d909a10be` |
| `2ecf-polar-log-radius-full-derivative-audit.py` | `91191c685481049caa2290c1cb3e3cecf8e7ebea17d063144a7663996eac61d5` |
| `polar-design-G10s-full-derivative-audit.json` | `0699f43185275ab010ecdd2872bfb0bf2a30ca7fb5bf2793b31bdb0a586f21fe` |
| `polar-design-G10s-full-derivative-audit-exit.json` | `5a2a114fef47ac8bed20449647235d80b0d9cab0516642e63994ed270b157dcc` |
| `2ecf-polar-log-radius-streamed-fd-design-solve.py` | `21a8766d2d3ef8038ee821e03077b8d43ba852e35702fc10725f647a396f993b` |
