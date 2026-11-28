# 完整新 g 设计的第5—8真步：独立曲率下降与仍未满足的 held guide

## 同一设计 epoch 的实际继续

接已发表 fast-normal 设计第4态，仍以同一源和 G10s prepared、12789 XYZ+87 log-radius共12876列、全部4291840行及原目标继续。`a=a0 exp(B alpha)` 的 alpha 仍为设计自由度；以下每次接受都改变 g，仅计本设计 epoch，不能冒原固定 g 或后续冻结 g 的收敛。

完整 sparse-jet normal 只重排所有角有限和，全部 XYZ/alpha 跨块、原曲率/几何/面积行和物理增量H2保持；每步仍由原完整 J/JT 检验实际 normal 方程。没有删除对 held 或曲率不利的行。

| 设计态 | 接受长度 | R14² | metric峰 | 自身κ峰 | min σ | min held | alpha∞ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | 1 | 0.040589522027968 | 0.32615257538972 | 81.852306997189 | 0.92571350068138 | 0.60584444512998 | 0.088345659428711 |
| 6 | 0.5 | 0.025378044088029 | 0.25417674948616 | 62.702115940759 | 0.94129875022435 | 0.60852584463043 | 0.089100338173825 |
| 7 | 0.25 | 0.019941956302288 | 0.22172381455838 | 48.088031945079 | 0.94003775351936 | 0.60745406476778 | 0.091463188066684 |
| 8 | 0.5 | 0.012302729310751 | 0.16687890626013 | 32.356091506914 | 0.943786777028 | 0.60714141700761 | 0.092021059140499 |

### 全部拒绝试值保留

| 设计步 | 实际被拒长度 | 这些长度的 R14² | 这些长度的自身κ |
|---|---|---|---|
| 5 | 无 | — | — |
| 6 | 1 | 0.062531806452542 | 135.1761052057 |
| 7 | 1, 0.5 | 0.1200131599743, 0.032309195165013 | 211.58348730192, 104.57298899218 |
| 8 | 1 | 0.022319050692951 | 72.723762373197 |

不是将更小 metric 峰直接当作接受；例如第6步整步的 metric 已较小，但总目标 .06253 高于输入 .04059，且 κ135.18，所以真实被拒。每步最终均经原全目标下降和 Armijo 条件接受。此四步外层尝试各1，末态累计设计 own8/8，继承的前4接受不重计。

| 设计步 | full normal相对残差 | λ used | λ next | 自然exit | 实际外部秒 | peak RSS KiB |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 4.3482507912163e-14 | 3.3333333333333e-05 | 3.3333333333333e-05 | 0 | 138.570635933 | 573696 |
| 6 | 4.440450758722e-14 | 3.3333333333333e-05 | 6.6666666666667e-05 | 0 | 138.504903141 | 583088 |
| 7 | 1.3309803555078e-13 | 6.6666666666667e-05 | 0.00013333333333333 | 0 | 162.219424434 | 566840 |
| 8 | 9.124147010358e-14 | 0.00013333333333333 | 0.00026666666666667 | 0 | 183.828198854 | 584564 |

## 每态自己的独立观察及目标 K

668径点×256半步错移角的 G11 在每个保存场上重新计算，使用该态同一 alpha；它仍不参与优化。目标 `K=-a''/a` 与位置的自身主曲率分开报告。

| 设计态 | G11 metric | G11自身κ | G11 σ | G11 held | G10目标 K绝对峰 | G11目标 K绝对峰 |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 0.32438268247219 | 82.320406292839 | 0.92597940858233 | 0.60602598094016 | 52.99885056009 | 51.573336825431 |
| 6 | 0.2525975425865 | 62.424946938603 | 0.94125780439226 | 0.60871928282319 | 55.852203472402 | 54.473039337015 |
| 7 | 0.22035089522812 | 47.888734025234 | 0.94022924015712 | 0.60763223970976 | 55.211034366914 | 53.793017968332 |
| 8 | 0.16364772854102 | 32.751706512341 | 0.94379713587134 | 0.60731779461589 | 53.498535198525 | 52.010264010074 |

各 G11 与目标审计均自然exit0；完整来源/退出哈希见下表。第8态 G10/G11 κ32.356/32.752 已较前态下降，但仍大于9.5 guide；它们都不是连续最大值。目标K样本约53不直接证明位置κ或 reach。

第5—8态原 held=.65 guide 分别仍违反约 .04416、.04147、.04255、.04286。第8态完整几何平方项为 .00010509986988516225；不能因它相对 metric/κ平方项较小而丢掉此责任。

### 当前 guide 与 README 全闭比例的准确对应

[R219](../results/R219-complete-low-wide-caps.md) 用完整新帽给的是 **全闭 D≤3.2**，不是把活动核 ball=1.59 误作整个面的 D≤3.18。原 held=.65 给最终完整排球 .64 留 .01 余量，.64/3.2=.2；width=.885 给整个闭面 .895 留 .01，R219支持凸包球1.0559给 δE≥.1609，故 δE/D≥.05028125；全闭 reach≥.097 才给 reach/D≥.0303125。当前 κguide9.5比1/.097更紧。

这些仍是完整原定理的条件，不是本条已经验证的闭族。当前第8 held样本 .60714 没有连续证书；即便以后对同一数值给出全核排球，它与 D≤3.2只给约.18973的下界，不能宣称.2强目标。准确等距、空间/网格加密、完整核非局部reach、固定H与全部时间、帽两jet拼接仍须支付。

## 完整重生命令

`S` 为公开 scripts，`W` 为包含原 prepared/source、完整 normal audit、G11缓存与已按前条重生第4态的工作目录。以下公开 driver 中，每步顺序调用实际 solve、G11和target audit，全部参数固定，并将每次真正returncode保留；它不会把未来步骤预先登记为成功。

```bash
python3 "$W/2ecf-polar-natural-process-receipt.py" --prefix "$W/polar-design-G10s-fast-steps05-08-driver" -- \
 python3 -u "$W/2ecf-polar-design-resume-driver.py" --scripts "$S" --work "$W" \
 --prepared "$W/polar-c2-G10s-prepared.json" --state "$W/polar-design-G10s-fast-step04-step01-state.json" \
 --observer "$W/polar-independent-G11r-shifted256-independent.json" \
 --normal-audit "$W/polar-G10s-sparse-jet-full-normal-audit.json" \
 --first 5 --stop 9 --tag polar-design-G10s-fast --boundary-pause-file "$W/polar-design-G10s-fast.pause"
```

生产入口 `2ecf-polar-log-radius-fast-normal-design-solve.py` SHA `21ce120289efa4f35decd7e7de120d501fa4392cb9bb4deb6c562e656662ea3d`；原完整 joint derivative 入口 SHA `f44226464ba3cad0f2c69f7bd9b7d86befa9a311d7ec268e0d81e7a19f36b17c`。本次实际调用是前条已说明的3至10连续调用中的第5—8自然返回；以上命令可单独重生相同物理步骤。新机器墙时与包含墙时的回执SHA自然可能不同，不能以计时差异篡改实际本轮记录。

| 文件 | SHA256 |
|---|---|
| `polar-design-G10s-fast-step05-step01-state.json` | `8d9da94e09593694fc3751dc3bef9d2f2538a04250392628a452a849d73df2ac` |
| `polar-design-G10s-fast-step05-exit.json` | `fa1fb74d38315508645ba2f765e9f6cadf6eb60facfdc92251e0f9c5d64c7db4` |
| `polar-design-G10s-fast-step05-G11.json` | `ea280fc5ae804dc8079dfb2436e5362221f195108b59e51a9c9c1864b6472c13` |
| `polar-design-G10s-fast-step05-G11-exit.json` | `f84c4f2962c1cb4e5c0f4d8692969515309829b41c4e15b6c908350e245ff915` |
| `polar-design-G10s-fast-step05-target-audit.json` | `bd621d54240c856f7a69b225a52020c3edaeea547410f26b86dd9af667d887f9` |
| `polar-design-G10s-fast-step05-target-audit-exit.json` | `4c3c3ad9ca2350e8c5e2b2807522e45c1966207d536a77813ef7dadac8b528ff` |
| `polar-design-G10s-fast-step06-step01-state.json` | `4bdc5065dfbbe8d03e172857bd46e9c3aaa6c9d04e82cd0352c826a820e2187c` |
| `polar-design-G10s-fast-step06-exit.json` | `716f2727be5ad8c10118a011790d481e9e7346a4734a425a5aa27bc642efc33a` |
| `polar-design-G10s-fast-step06-G11.json` | `0dc1cdf6bfce5d8c2651d86e45879c37e3b68bce1d9fca60f852d31c44809c73` |
| `polar-design-G10s-fast-step06-G11-exit.json` | `69af44309e028eed687d75d642dbc3a3c7040b0ca52de4563526df6509536466` |
| `polar-design-G10s-fast-step06-target-audit.json` | `07bb2187a4b0728b1fb1d81594c5f63d6b80269e7a8674e628cb0013943312cb` |
| `polar-design-G10s-fast-step06-target-audit-exit.json` | `7cc649b3ca202d41fde3fda0448a620f1a52596c339585189171af749f8e8b10` |
| `polar-design-G10s-fast-step07-step01-state.json` | `396fe2f485ef8d503a7677d09b1d3e66897a5638c6576668d02988c73e40b76b` |
| `polar-design-G10s-fast-step07-exit.json` | `f8358eec9ae1a21dbd0edcb0c20938785e3f7454922333e25b3ef3987e5b1a6a` |
| `polar-design-G10s-fast-step07-G11.json` | `8063ab5907576ef5f8e9d78da059fd478143ce4b657cfdec545ebca56e92ffde` |
| `polar-design-G10s-fast-step07-G11-exit.json` | `ed04af97c1d0e03e80fc666ad5b8ac83f621a6a3aca54a98bd46c561c2438e4b` |
| `polar-design-G10s-fast-step07-target-audit.json` | `a71922ef7280528e0fc4ec6c847d96e628e17531f2cce767e7dd710246fd7263` |
| `polar-design-G10s-fast-step07-target-audit-exit.json` | `c0aa5e5d5df892a8fd488e79d3937e37044b506e9e158520b5072e1fdfb839a6` |
| `polar-design-G10s-fast-step08-step01-state.json` | `a8b4ce37ed285d29e57470293b7bdb5db163da28f18b6b38cf4bc5bf0539d97f` |
| `polar-design-G10s-fast-step08-exit.json` | `7df7c4e5f7421524b1445503a69ca213522f354e1902c1a00ced80690091681d` |
| `polar-design-G10s-fast-step08-G11.json` | `204e0650a708287e4a6157d5125180f2d0e72f147006dbdab2af8d867142e52b` |
| `polar-design-G10s-fast-step08-G11-exit.json` | `0554fb5f67488d2ab051e2b0c9193c07a7f4c04807a93b8a62357fe60e7b2a40` |
| `polar-design-G10s-fast-step08-target-audit.json` | `6edcc5f20f50bdfbba69ce466c8932de521d06143feed4265f5d1eb1ace7a993` |
| `polar-design-G10s-fast-step08-target-audit-exit.json` | `726c7dfa5abbad9b155b3bc3e1d5cbbca286d4193cb92e886ace65082e32cb82` |
