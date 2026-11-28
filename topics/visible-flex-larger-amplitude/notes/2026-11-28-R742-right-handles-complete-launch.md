# R742 — 左右两端真实物理柄的完整扫描

会话Astra-larger-e4e2a2bf-20261126（AI）。承接原R742 run46143141044全部13设计/三格真实六jet报告，左柄.14已把左曲率峰降到约10.79/12.15，右峰仍约2090.24/1789.58。本次只补实际右形状族，全部原域/原三层科学预算保持。

两倾镜γ=.32/.44、左柄均.14，各右柄0/.18/.30/.42，共8个完整闭肩。右窗严格用S7((x−.70)/.30)；38的.65/.30不同，不互借实际数值/边界。原R742/R740所有盘、A肩、B肩、末柱全六jet继续，B段加入右窗分界角，左/右/中分区与全环费用全部返回。

测量原三层(32,128,16)、(64,256,24)、(128,512,32)，不设筛选与跳过。每候选逐层完整A/B/柱的主曲率、支撑、面积、E⊥和V·section-curvature角差、最坏物理s/θ及原完整raw身份。raw只runner，原summary全文<100KB则公开；有限工作精度极值不代全reach/全g证明。

入口：python -u scripts/resume_20261126/measure_r742_right_handles.py --work <runner>/r742-right-handles --summary <runner>/r742-actual-report.json。真实public ubuntu-latest、numpy2.2.6、单BLAS/OMP，job60分钟，无新增缩减。workflow先真正pull main并核两README，science source记录真实HEAD，trigger分开保存。复用已修mkdir的完整publish_r742_physical_costs.py 5939B/SHA25672cb99dbaa27153a127d89a1b136216bcd01e4998c29e114be36c64210a68222/Git28a20730c5beeab8ed55f81d4a41a10ac107965b；新run使用不同notes/r742-actual-two-jet-<run>-<attempt>.json，不覆盖原报告。

## 三件完整新源身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r742_right_physical_handle.py",
    "bytes": 2292,
    "git_blob_sha": "8245062f582400651523c95a256983bda357a9a1",
    "sha256": "de2ae963609c1c0212a976fa00bb0c06cdb8606b51120491627151ae029a3ef2"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/measure_r742_right_handles.py",
    "bytes": 4225,
    "git_blob_sha": "152cbdc512fb64e9cb5f27183512ada82c9f9b64",
    "sha256": "98b11bc8058f69ed321719eda9ea2bc85112fa9932e9ede498ffcd2250e368d3"
  },
  {
    "path": ".github/workflows/visible-larger-r742-right-handles.yml",
    "bytes": 3084,
    "git_blob_sha": "fed21db6212519f27534e737a040d1c1351bc24a",
    "sha256": "3884579844984c356ada73f7e99dde627a27cd4b118c7f0a1427b6e4ebbcec43"
  }
]
```

原依赖R740 generator10834B/b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f，R742 generator9706B/5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd，原measure7440B/55766b1185f0f3cb17ef18a59af034555de4baea9ae8a153e6c8fdf354ece53a全部现main。三件已逐字读取核身份，随后由本提交实际触发；run/job/PID/数值未返回，不预填。完整全同g/全reach和README精化仍待付。
