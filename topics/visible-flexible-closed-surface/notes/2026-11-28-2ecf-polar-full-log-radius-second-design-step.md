# 完整log-radius设计第2真步：目标K继续单列，held guide已出现违差

同一新g设计epoch、同一958径点两完整角组、全部12789 XYZ+87 alpha列和4291840个原13+q2行继续。不是原固定g改善；alpha仍为待冻结设计变量。source、物理basis/weights、全H2、全部正规跨块和原非线性接受规则保持。

λ=1e−4，完整物理normal相对残差8.70834855707e−15，slope=−2.78113946350、预测全步下降2.78125248943。真实长度1接受，设计own次数1→2，下一λ保持1e−4。完整normal段321.366374066秒。

| 有限G10指标 | 设计第1态 | 设计第2态 |
|---|---:|---:|
| R14² | 2.8213951569423905 | 0.8899201406196648 |
| metric峰 | 1.5951072356069562 | 1.0606094323878104 |
| own-curvature峰 | 711.5980234983732 | 130.10277297749576 |
| min sigma | 0.5785521747622492 | 0.6881947601910205 |
| min held | 0.660345224779596 | 0.6336494515370386 |
| alpha infinity norm | 0.056460664242215436 | 0.07893787657178086 |

原held=.65的guide在新场出现真实最大违差.016350548462961467，geometry R²=5.340488653757563e−6；metric/curvature分项分别.7746776524249608/.11523714770605056，area=0。全部原约束行继续参与成本，**接受仅为完整成本下降，不宣称满足全部geometry guides**。不会隐藏这项局部退化或把held样本直接当归一化全曲面证书。

独立G11的668×256错移角观察：metric1.0616757783558672、κ133.3061913647739、σ.7015156192505994。κ热点在s=.14519289341741065,u=.4049709280018093；未进入训练的540径点与全部错移角继续实际消费，未用于接受判据。

同保存alpha的target诊断继续重付：G10/G11最大|K|样本46.0697333466/46.2853573955（均负K），相比第1态48.145/48.049略降。目标a最大样本约1.102728，未保持原目标g。准确有理全域h/h′/h″/分片h‴上界的小数展示为.07893787657/.983734925893/114.284751987/114135.922051；准确分数在JSON。准确h端点两jet为0，仍没有原a0全部连续界，因此不是连续K上界。

三个实进程：solve自然0/336.057521220秒/RSS626692KiB；G11自然0/1.249898016秒/RSS114008KiB；target audit自然0/.632816190秒/RSS89220KiB。本条新增设计接受1、该epoch累计2，与固定g接受链分开。完整alpha仍待选择/冻结和真正同g加密。

第3步已用通过全G10/JᵀJ审计的稀疏角normal新消费者继续；其具体实现迁移只允许normal/solver实现SHA变化，并重算与旧第2态完全相同的baseline和groups，继承2次接受不重计。新物理步需再次实际支付全部normal/非线性/独立G11/target诊断。其结果另记，不写入本条第2态。

复现本步仍用 `2ecf-polar-log-radius-streamed-fd-design-solve.py --state ...fd-step01-step01-state.json --prefix ...fd-step02 --steps 1`，其余完整参数与第1态note相同；G11与target audit均指向新第2态。

| 文件 | SHA256 |
|---|---|
| `polar-design-G10s-fd-step02-step01-state.json` | `97d42d5c54cbbb0bd8379978b3dd8fb93b663c2a22e16198f9baea8410147120` |
| `polar-design-G10s-fd-step02-exit.json` | `26689a0487afd9e4458ad8df1ca623ef19e976af399171f0ef5faa87a4e9f19b` |
| `polar-G11r-design-G10s-fd-step02.json` | `6c36e9abbc07082184da1d7451fbedf4c8232d86ac681eed1e449528d852ef86` |
| `polar-G11r-design-G10s-fd-step02-exit.json` | `fa096cfc8a722fa49664d1e110eb958957881de1f53b167dc002cbedf9dd37ca` |
| `polar-design-G10s-fd-step02-target-audit.json` | `a66120a7ac2b56d023c7a6d7a955da34b716cef9cff531d12c875104515ecb8c` |
| `polar-design-G10s-fd-step02-target-audit-exit.json` | `51768627d39bd05b5c0a03e185856545bc9f19168aab7d6355d9de5b1cb4dde7` |
